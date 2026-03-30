import pandas as pd
import os

df = pd.read_csv("data/silver/clean_weather.csv")
os.makedirs("data/gold", exist_ok=True)

result = df.groupby("city")["temp"].mean().reset_index()
result.to_csv("data/gold/avg_temp.csv", index=False)
print("Gold layer created")
