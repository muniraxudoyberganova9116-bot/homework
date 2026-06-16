"""
Task 2 — Scrape job listings from https://realpython.github.io/fake-jobs
and store them in SQLite with incremental loading + update tracking.

Install first:  pip install requests beautifulsoup4
Run:            python task2_jobs.py
"""

import csv
import sqlite3

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
DB_NAME = "jobs.db"


# ---------- 1. Scraping ----------
def scrape_jobs():
    """Scrape all job listings from the page and return a list of dicts."""
    response = requests.get(URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for card in soup.find_all("div", class_="card-content"):
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()

        # The "Apply" link is the second <a> in the footer
        links = card.find_all("a")
        apply_link = links[1]["href"] if len(links) > 1 else links[0]["href"]

        # The fake-jobs cards don't show a description on the list page,
        # so we fetch it from the job's detail page (the Apply link).
        detail = requests.get(apply_link)
        detail_soup = BeautifulSoup(detail.text, "html.parser")
        desc_tag = detail_soup.find("div", class_="content").find("p")
        description = desc_tag.text.strip() if desc_tag else ""

        jobs.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "description": description,
                "link": apply_link,
            }
        )
    return jobs


# ---------- 2. Database setup ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
        """
    )
    conn.commit()
    return conn


# ---------- 3 & 4. Incremental load + update tracking ----------
def load_jobs(conn, jobs):
    cur = conn.cursor()
    inserted, updated, unchanged = 0, 0, 0

    for job in jobs:
        cur.execute(
            "SELECT id, description, link FROM jobs "
            "WHERE title=? AND company=? AND location=?",
            (job["title"], job["company"], job["location"]),
        )
        row = cur.fetchone()

        if row is None:
            # New job -> insert
            cur.execute(
                "INSERT INTO jobs (title, company, location, description, link) "
                "VALUES (?, ?, ?, ?, ?)",
                (job["title"], job["company"], job["location"],
                 job["description"], job["link"]),
            )
            inserted += 1
        else:
            job_id, old_desc, old_link = row
            # Existing job -> check if anything changed
            if old_desc != job["description"] or old_link != job["link"]:
                cur.execute(
                    "UPDATE jobs SET description=?, link=? WHERE id=?",
                    (job["description"], job["link"], job_id),
                )
                updated += 1
            else:
                unchanged += 1

    conn.commit()
    print(f"Inserted: {inserted}, Updated: {updated}, Unchanged: {unchanged}")


# ---------- 5. Filtering + CSV export ----------
def filter_jobs(conn, location=None, company=None):
    """Return jobs filtered by location and/or company (partial match)."""
    query = "SELECT title, company, location, description, link FROM jobs WHERE 1=1"
    params = []
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    return conn.execute(query, params).fetchall()


def export_to_csv(rows, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} rows to {filename}")


# ---------- Main ----------
if __name__ == "__main__":
    conn = init_db()

    print("Scraping jobs...")
    jobs = scrape_jobs()
    print(f"Found {len(jobs)} jobs on the page.")

    load_jobs(conn, jobs)

    # Example: filter by location and export to CSV
    results = filter_jobs(conn, location="Stewartbury")
    for r in results:
        print(r[0], "|", r[1], "|", r[2])
    export_to_csv(results, "stewartbury_jobs.csv")

    conn.close()