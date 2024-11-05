import requests
import pandas as pd


response = requests.get("https://api.spacexdata.com/v4/rockets")

data = response.json()

data = pd.DataFrame(data)

print(data)
print(data.shape)
print(data.columns)
print(data.info())
