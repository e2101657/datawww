import pandas as pd
import os

os.makedirs("data/silver", exist_ok=True)


realtime = pd.read_csv("data/bronze/realtime_weather.csv")
historical = pd.read_csv("data/bronze/vaasa_historical.csv")


realtime = realtime.rename(columns={"temperature": "temp"})
historical = historical.rename(columns={"temp_max": "temp"})


realtime["city"] = "Vaasa"
historical["city"] = "Vaasa"


df = pd.concat([realtime, historical], ignore_index=True)


df = df.fillna(0)


df.to_csv("data/silver/clean_weather.csv", index=False)

print("Silver layer created")
    
    
    