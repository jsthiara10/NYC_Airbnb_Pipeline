from src.pipeline import clean_airbnb_data
from pathlib import Path

if __name__ == "__main__":
    # Use relative paths from the root of the project
    input_path = "data/raw/AB_NYC_2019.csv"
    output_path = "data/cleaned/AB_NYC_2019_cleaned.csv"

    clean_airbnb_data(input_path, output_path)
