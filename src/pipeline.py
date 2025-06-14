import pandas as pd
import regex as re

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
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def clean(self):
        self.drop_duplicates()
        self.drop_nulls()
        self.clean_host_name()
        return self.df

    def drop_duplicates(self): # drop duplicate rows
        self.df.drop_duplicates(inplace=True)

    def drop_nulls(self): # drops nulls values
        self.df.dropna(inplace=True)




# 1. we have names such as 'MaryEllen'. I want to split those strings by doing something like 'Mary Ellen'.

# def split_camel_case(name):
#     return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)

# 2. next, i want to replace 'and' with a & in those columns
