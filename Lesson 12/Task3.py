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