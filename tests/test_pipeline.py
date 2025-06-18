import pandas as pd
from src.pipeline import AirbnbCleaner


def test_clean_airbnb_data(tmp_path):
    # Dummy raw dataset with nulls and duplicates
    raw_data = {
        "id": [1, 2, 2, 3],
        "name": ["Listing A", "Listing B", "Listing B", None],
        "price": [100, 150, 150, 200],
        "host_name": ["MaryEllen", "johnSmith", "johnSmith", "Mike and Lily"],
        "number_of_reviews": [0, 5, 5, 1]
    }
    raw_df = pd.DataFrame(raw_data)

    # Run the cleaning pipeline
    cleaner = AirbnbCleaner(raw_df)
    cleaned_df = cleaner.clean()

    # Save to temporary file to mimic I/O behavior
    cleaned_file = tmp_path / "cleaned.csv"
    cleaned_df.to_csv(cleaned_file, index=False)

    # Load cleaned CSV and run assertions
    result = pd.read_csv(cleaned_file)

    assert result.shape[0] == 1 # Duplicate, nulls and zeroes removed
    assert result["name"].isnull().sum() == 0
    assert result["name"].isnull().sum() == 0
    assert result["id"].duplicated().sum() == 0

    # Optional: Check host_name normalization
    expected_names = ["John Smith"]
    assert result["host_name"].tolist() == expected_names
