# Vazeem-Internship-2026

zellbytes internship work





\#mushroom-yield-project -day1

\# Mushroom Yield Project



\## Environment Setup



1\. Create virtual environment

&#x20;  python -m venv venv



2\. Activate virtual environment

&#x20;  venv\\Scripts\\activate



3\. Install dependencies

&#x20;  pip install pandas numpy matplotlib scikit-learn jupyter



4\. Run smoke test

&#x20;  python src\\smoke\_test.py

&#x20;

\## Project Overview-day2



This project predicts mushroom yield using Python and machine learning.



\## Folder Structure



\- data/raw

\- models

\- outputs

\- src



\## Project overview ## -day3



loaded ingest.py file into src

The objective of ingest.py in a data project is usually to load raw data and prepare it for further processing.

&#x20;

&#x20;ingest.py load the raw polyhouse sensor CSV, perform initial validation/conversion, and save it in a structured format (Parquet) for  downstream data processing and machine learning tasks.



rest of the workflow follows these steps

Raw Sensor Data

&#x20;      ↓

ingest.py

&#x20;      ↓

01\_loaded.parquet

&#x20;      ↓

clean.py / preprocess.py

&#x20;      ↓

feature engineering

&#x20;      ↓

train.py

&#x20;      ↓

yield prediction model



\##  cleaning  ## day-4



loaded clean.py file into src



This script performs data cleaning and preprocessing using several common techniques:

1 Missing value analysis

2 Range-based filtering (data validation)
3 Null target removal

4 Forward-fill imputation

5 Deletion of missing targets

6 Deduplication



Overall Cleaning Strategy



This is a combination of:



1 Data Validation Cleaning

&#x20; Filters out out-of-range sensor readings.

2 Missing Value Treatment

&#x20; Forward-fill imputation for sensor data.

&#x20; Row deletion for missing target values.

3 Data Deduplication

&#x20; Removes duplicate timestamps.

4 Quality-Based Filtering

&#x20; Retains only records that satisfy predefined oyster polyhouse environmental conditions.



Duplicate records were identified using the timestamp column and removed while retaining the latest occurrence. A total of 0 duplicate records were removed, resulting in a final cleaned dataset containing 365 rows.



02\_cleaned.parquet was successfully loaded and validated. The target column (yield\_kg) contains 0 missing values, confirming that all records are suitable for downstream analysis and model training.



\## Data Quality Report Generation ## -day5



\### Objective



The objective of this script is to perform an exploratory assessment of the cleaned polyhouse sensor dataset and automatically generate a data quality report.



\### Tasks Performed



1\. Loads the cleaned dataset (`02\_cleaned.parquet`).

2\. Calculates summary statistics for:



&#x20;  \* Temperature

&#x20;  \* Humidity

&#x20;  \* CO₂ concentration

&#x20;  \* Mushroom yield

3\. Computes the coefficient of variation (CV) to measure relative variability.

4\. Compares mean and median values to identify potential data skewness.

5\. Generates human-readable insights describing the distribution of each feature.

6\. Creates a Markdown report containing:



&#x20;  \* Dataset size

&#x20;  \* Date range

&#x20;  \* Summary statistics table

&#x20;  \* Distribution insights

7\. Saves the report as:



```text

reports/data\_quality.md

```



\### Output



The generated report provides a concise overview of data quality and feature distributions, helping validate the dataset before feature engineering, visualization, and machine learning model development.







