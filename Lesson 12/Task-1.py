import requests
from bs4 import BeautifulSoup
import sqlite3

response = requests.get("https://realpython.github.io/fake-jobs/")
response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser") 
jobs = soup.find_all("div", class_="card-content")
print(len(jobs))
title = jobs[0].find("h2", class_="title").text.strip()
company = jobs[0].find("h3", class_="company").text.strip()
location = jobs[0].find("p", class_="location").text.strip()
print(title, company, location)

all_jobs = []
for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    all_jobs.append({"title": title, "company": company, "location": location})

print(len(all_jobs))
print(all_jobs[0])

conn = sqlite3.connect("my_jobs.db")
cursor = conn.cursor()
print("Database connected!")

for job in all_jobs:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            UNIQUE(title, company, location)
        )
""")
print("Table created!")

cursor.execute(
    "INSERT OR IGNORE INTO jobs (title, company, location) VALUES (?, ?, ?)",
    (job["title"], job["company"], job["location"])
)
cursor.execute("SELECT * FROM jobs")
rows = cursor.fetchall()
print(len(rows))
print("Jobs inserted!")
conn.commit()
