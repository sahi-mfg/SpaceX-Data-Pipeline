import pandas as pd


data = {
    "rocket": ["Falcon 9", "Falcon 1", "Falcon Heavy"],
    "launches" : [100, 5, 3],
}

df = pd.DataFrame(data)

print(df)


# Data manipulation

# Selecting a column
print(df["rocket"])

# filtering rows
falcon9_df = df[df["rocket"] == "Falcon 9"]

# Adding a new column
df["success_rate"] = [0.95, 0.5, 0.33]