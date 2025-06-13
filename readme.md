# **🧼 Project Overview**

**NYC Airbnb Data Cleaning Pipeline** is a data engineering project that processes raw Airbnb listing data from New York City and transforms it into a clean, structured, and analysis-ready format.

**The goal** of this project is to simulate a real-world ETL pipeline using Python and pandas. It reads a raw CSV file, performs a series of cleaning and transformation steps — including handling missing values, fixing data types, removing duplicates, normalizing column names, and filtering invalid entries — and then outputs a cleaned CSV for use in analytics, visualization, or machine learning workflows.

This project demonstrates key data engineering skills such as:

Working with messy real-world data

Building modular, reusable pipeline code

Designing reproducible data processing workflows

Preparing datasets for downstream analysis

The cleaned data can be used to power dashboards, generate business insights, or serve as the input for predictive models (e.g., estimating nightly prices, predicting availability, etc.).



## **Folder Structure**



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
