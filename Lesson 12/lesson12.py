"""
Task 1 — Scrape weather info from weather.html using BeautifulSoup.
Run:  python task1_weather.py
(weather.html must be in the same folder)
"""

from bs4 import BeautifulSoup

# 1. Parse the HTML file
with open("/home/zhav3n/Desktop/homework/Lesson 11/HOMEWORK/Lesson 12/weather.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = soup.find("table").find("tbody").find_all("tr")

forecast = []
for row in rows:
    cells = row.find_all("td")
    day = cells[0].text.strip()
    temp = int(cells[1].text.strip().replace("°C", ""))
    condition = cells[2].text.strip()
    forecast.append({"day": day, "temp": temp, "condition": condition})

# 2. Display weather data
print("=== 5-Day Weather Forecast ===")
for entry in forecast:
    print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

# 3a. Day(s) with the highest temperature
max_temp = max(entry["temp"] for entry in forecast)
hottest_days = [e["day"] for e in forecast if e["temp"] == max_temp]
print(f"\nHighest temperature: {max_temp}°C on {', '.join(hottest_days)}")

# 3b. Day(s) with "Sunny" condition
sunny_days = [e["day"] for e in forecast if e["condition"] == "Sunny"]
print(f"Sunny days: {', '.join(sunny_days)}")

# 4. Average temperature
avg_temp = sum(e["temp"] for e in forecast) / len(forecast)
print(f"Average temperature: {avg_temp:.1f}°C")




#task2 
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

#task3

"""
Task 3 — Scrape laptops from https://www.demoblaze.com/ (Laptops section,
then the Next page) using Selenium, and save the data to JSON.

Install first:  pip install selenium webdriver-manager
Requires Chromium installed:  sudo pacman -S chromium
Run:            python Task3.py
"""

import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.demoblaze.com/"


def scrape_laptops_on_page(driver):
    """Scrape name, price, description for every laptop card on the current page."""
    # Wait until cards are present
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card"))
    )
    time.sleep(1)  # small buffer so the page fully refreshes

    laptops = []
    cards = driver.find_elements(By.CLASS_NAME, "card")
    for card in cards:
        name = card.find_element(By.CLASS_NAME, "card-title").text.strip()
        price = card.find_element(By.TAG_NAME, "h5").text.strip()
        description = card.find_element(By.CLASS_NAME, "card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})
    return laptops


def main():
    # Set up Chromium (headless so no browser window pops up)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/chromium"  # Arch Linux Chromium path
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    try:
        # 1. Open the homepage
        driver.get(URL)

        # 2. Click the "Laptops" category
        wait = WebDriverWait(driver, 10)
        laptops_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Laptops"))
        )
        laptops_link.click()
        time.sleep(2)  # wait for products to load

        all_laptops = []

        # Scrape page 1 of the Laptops section
        all_laptops.extend(scrape_laptops_on_page(driver))

        # 3. Click "Next" and scrape page 2
        next_button = wait.until(EC.element_to_be_clickable((By.ID, "next2")))
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(2)
        all_laptops.extend(scrape_laptops_on_page(driver))

        # Remove possible duplicates (same laptop appearing twice)
        unique = {laptop["name"]: laptop for laptop in all_laptops}
        all_laptops = list(unique.values())

        # 4. Save to JSON
        with open("laptops.json", "w", encoding="utf-8") as f:
            json.dump(all_laptops, f, indent=2, ensure_ascii=False)

        print(f"Scraped {len(all_laptops)} laptops -> laptops.json")
        for laptop in all_laptops:
            print(f"- {laptop['name']} | {laptop['price']}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()