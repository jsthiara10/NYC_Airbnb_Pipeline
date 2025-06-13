import pandas as pd


def clean_airbnb_data(input_path: str, output_path: str) -> None:
    """
    Reads raw Airbnb data, cleans it by dropping duplicates and nulls,
    then saves the cleaned data to a new CSV.

    Parameters:
        input_path (str): Path to the raw CSV.
        output_path (str): Path where the cleaned CSV will be saved.
    """
    df = pd.read_csv(input_path)

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows with any null values
    df = df.dropna()

    # Save cleaned DataFrame
    df.to_csv(output_path, index=False)

    print("Data has been cleaned and written to a new CSV")

