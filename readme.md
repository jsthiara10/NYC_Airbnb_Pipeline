````bash
NYC_Airbnb_Pipeline/
├── data/
│   ├── raw/                 # Original CSV files (e.g., from Kaggle)
│   └── cleaned/             # Output from the cleaning pipeline
├── notebooks/
│   └── EDA.ipynb            # Exploratory Data Analysis
├── src/
│   ├── __init__.py
│   ├── pipeline.py          # Core pipeline logic (ETL steps)
│   └── utils.py             # Helper functions (e.g., renaming, parsing)
├── tests/
│   └── test_pipeline.py     # Unit tests for your pipeline
├── main.py                  # Entry point for running the pipeline
├── requirements.txt         # Python dependencies
├── README.md                # Project overview and instructions
├── .gitignore               # Files to ignore in Git
└── .env (optional)          # If you ever add configs or API keys
```
