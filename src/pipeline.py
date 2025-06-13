import pandas as pd

csv_path = "/Users/jsthiara/Desktop/NYC_Airbnb_Pipeline/data/raw/AB_NYC_2019.csv"
df = pd.read_csv(csv_path)

print(df.head())

"""1. First, let's drop duplicates"""

df.drop_duplicates()

"""2. Secondly, let's remove nulls"""

df.dropna()

print(df.head())


"""2. Write this to a csv to test it is working """

# cleaned.to_csv("/Users/jsthiara/Desktop/NYC_Airbnb_Pipeline/data/cleaned/AB_NYC_2019_cleaned.csv", index=False)

# print("New data Written to CSV")

### TO DO ###:

# 1. Remove duplicates

# 2. Remove nulls

# 3. Convert text and numeric fields to consistent formats e.g. price/dates

# 4. Filter Outliers and invalid entries

