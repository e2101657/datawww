import requests
import time
import pandas as pd
import os

API_KEY = "85cb05c3ad934357825104555263003"
CITY = "Vaasa"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

file_path = "data/bronze/realtime_weather.csv"

os.makedirs("data/bronze", exist_ok=True)

while True:
    response = requests.get(url)
    data = response.json()

    weather = {
        "temperature": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"],
        "timestamp": data["location"]["localtime"]
    }

    print(weather)

    df = pd.DataFrame([weather])

   
    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode="a", header=False, index=False)

    time.sleep(60)