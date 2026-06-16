from bs4 import BeautifulSoup

# 1. Parse the HTML file
with open("/home/zhav3n/Desktop/homework/Lesson 12/weather.html", "r", encoding="utf-8") as f:
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