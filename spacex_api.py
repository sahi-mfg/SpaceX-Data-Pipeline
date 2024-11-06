import pandas as pd


url: str = "https://api.spacexdata.com/v4/rockets"

data: pd.DataFrame = pd.read_json(url)


print(data.head())
print(data.columns)

print(data.dtypes)
