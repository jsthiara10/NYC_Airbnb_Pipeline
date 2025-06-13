import pandas as pd
import os
from src.pipeline import clean_airbnb_data


def test_clean_airbnb_data(tmp_path):
    # Create a dummy raw dataset with nulls and duplicates
    raw_data = {
        "id": [1, 2, 2, 3],
        "name": ["Listing A", "Listing B", "Listing B", None],
        "price": [100, 150, 150, 200]
    }
    raw_df = pd.DataFrame(raw_data)

    # Set paths
    raw_file = tmp_path / "raw.csv"
    cleaned_file = tmp_path / "cleaned.csv"

    # Save raw CSV
    raw_df.to_csv(raw_file, index=False)

    # Run the cleaning function
    clean_airbnb_data(str(raw_file), str(cleaned_file))

    # Load the cleaned CSV
    cleaned_df = pd.read_csv(cleaned_file)

    # Assert that nulls and duplicates are removed
    assert cleaned_df.shape[0] == 2  # Only rows 1 and 2 should remain
    assert cleaned_df["name"].isnull().sum() == 0
    assert cleaned_df["id"].duplicated().sum() == 0
