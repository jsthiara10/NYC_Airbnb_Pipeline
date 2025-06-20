import pandas as pd
import regex as re
import argparse

"""
🧠 Conceptual Overview:
-----------------------
Think of the `AirbnbCleaner` class like a video game character (CleanBot).

- The class itself is the character.
- The `clean()` method is the character's ultimate move — a combo of multiple actions.
- Each helper method (e.g., `drop_duplicates`, `drop_nulls`, `clean_host_name`) is one of the character's abilities.
- These abilities are executed in sequence when `clean()` is called.
- `self.df` is the "scroll" or data the character is cleaning and carrying through the game.

This object-oriented structure helps organize the pipeline clearly, makes it easier to maintain,
and sets up a solid foundation for scaling, testing, and CI/CD integration.
"""


class AirbnbCleaner:
    def __init__(self, df: pd.DataFrame): # the constructor takes the pandas df as input and makes a copy of it to
        # avoid modifying the original
        self.df = df.copy()

    def clean(self): # these apply all the individual cleaning steps in order
        self.drop_duplicates()
        self.drop_nulls()
        self.clean_host_name()
        self.remove_zero_reviews()
        return self.df

    def drop_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def drop_nulls(self):
        self.df.dropna(inplace=True)

    def clean_host_name(self):
        def clean_name(name):
            if pd.isnull(name):
                return name
            name = str(name).strip()
            name = self._split_camel_case(name)
            name = self._replace_and(name)
            name = name.title()
            return name

        self.df["host_name"] = self.df["host_name"].apply(clean_name)

    def _split_camel_case(self, name: str) -> str: # makes strings consistent e.g. John Smith, instead of 'John smith'
        return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", name)

    def _replace_and(self, name: str) -> str:
        return re.sub(r"\band\b", "&", name, flags=re.IGNORECASE)

    """Remove listings that have 0 number of reviews"""

    def remove_zero_reviews(self):
        self.df = self.df[self.df["number_of_reviews"] > 0]


# 🧪 CLI Runner
def run_pipeline(input_path, output_path):
    df = pd.read_csv(input_path)
    cleaner = AirbnbCleaner(df)
    cleaned_df = cleaner.clean()
    cleaned_df.to_csv(output_path, index=False)
    print("✅ Data cleaned and saved to:", output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the raw input CSV")
    parser.add_argument("--output", required=True, help="Path to save the cleaned CSV")
    args = parser.parse_args()

    run_pipeline(args.input, args.output)
