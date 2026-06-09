import requests

API_KEY = "bf5c8bbf8cdbd31f8317b3dce5eb188f"  
print(f"Using key: {API_KEY}")
CITY = "Tashkent"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {CITY}:")
    print(f"  Temperature: {data['main']['temp']}°C")
    print(f"  Feels like:  {data['main']['feels_like']}°C")
    print(f"  Humidity:    {data['main']['humidity']}%")
    print(f"  Conditions:  {data['weather'][0]['description']}")
    print(f"  Wind speed:  {data['wind']['speed']} m/s")
else:
    print(f"Error {response.status_code}: {data.get('message')}")