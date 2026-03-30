import requests
import pandas as pd
import os


lat = 63.10
lon = 21.62

url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date=2020-03-30&end_date=2020-04-30&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temp_max": data["daily"]["temperature_2m_max"],
    "temp_min": data["daily"]["temperature_2m_min"]
})

os.makedirs("data/bronze", exist_ok=True)
df.to_csv("data/bronze/vaasa_historical.csv", index=False)

print("Vaasa historical data loaded")
