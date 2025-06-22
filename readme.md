# **🏡 NYC Airbnb Data Cleaning Pipeline**

This project is a lightweight, testable, and extensible data pipeline that cleans and transforms raw NYC Airbnb listings into structured data ready for analysis or machine learning.

## 📦 Features

✅ Object-oriented cleaning with AirbnbCleaner class

✅ Handles nulls, duplicates, inconsistent naming conventions

✅ Converts camelCase to title case and replaces "and" with &

✅ Drops listings with 0 reviews

✅ Creates separate sheets by neighbourhood group (coming soon)

✅ Automated testing with pytest and CI via GitHub Actions

✅ Scheduled daily runs with cron on local machine

✅ Logging for data quality monitoring

## 🧰 Tech Stack

Python 3.11+

pandas

pytest

GitHub Actions (CI)

cron (for scheduled local runs)

Google Cloud (coming soon)

## 🚀 Getting Started

## 1. Clone the repo
```
git clone https://github.com/jsthiara10/NYC_Airbnb_Pipeline.git
cd NYC_Airbnb_Pipeline
```

## 2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
## 3. Install dependencies
```
pip install -r requirements.txt
```
## 4. Run the pipeline
```
python main.py
```
This will read the raw Airbnb dataset from data/raw/AB_NYC_2019.csv, clean it using AirbnbCleaner, and write the result to data/cleaned/AB_NYC_2019_cleaned.csv.

## ✅ Running Tests
```
PYTHONPATH=. pytest
```
All tests live in the /tests folder and validate data cleaning behaviors like null removal, duplicate dropping, and host name formatting.

## 🤖 GitHub Actions (CI)

This repo uses GitHub Actions to automatically run tests on every push or pull request to main.

CI config lives in: .github/workflows/ci.yml

## ⏰ Automating the Job with Cron

You can schedule the pipeline to run automatically on your Mac using a cron job.

Example: Run daily at 11:50 AM
```
crontab -e
```
Add:
```
50 11 * * * /path/to/venv/bin/python /path/to/NYC_Airbnb_Pipeline/main.py
```
☁️ Cloud Deployment (Coming Soon)

Planned future setup includes:

Migrating the pipeline to run in the cloud (e.g., GCP Cloud Functions or Cloud Run)

Uploading cleaned data to Google Cloud Storage

Monitoring and alerting via GCP tools

## 📌 Roadmap

TBC

## 👨‍💼 Author

Built by Jasraj Singh Thiara

Feel free to connect or contribute!
