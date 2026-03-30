import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv("data/silver/clean_weather.csv")


df = df.reset_index()

X = df[["index"]]
y = df["temp"]


model = LinearRegression()
model.fit(X, y)


pred = model.predict(X)

print("Model trained")
print(pred[:5])