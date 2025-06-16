import pandas as pd
from src.pipeline import AirbnbCleaner

input_path = "data/raw/AB_NYC_2019.csv"
output_path = "data/cleaned/AB_NYC_2019_cleaned.csv"

df = pd.read_csv(input_path)
cleaner = AirbnbCleaner(df)
cleaned_df = cleaner.clean()
cleaned_df.to_csv(output_path, index=False)

