# Vazeem-Internship-2026

zellbytes internship work





#mushroom-yield-project -day1

# Mushroom Yield Project



## Environment Setup



1\. Create virtual environment

&#x20;  python -m venv venv



2\. Activate virtual environment

&#x20;  venv\\Scripts\\activate



3\. Install dependencies

&#x20;  pip install pandas numpy matplotlib scikit-learn jupyter



4\. Run smoke test

&#x20;  python src\\smoke\_test.py

&#x20;

## Project Overview-day2



This project predicts mushroom yield using Python and machine learning.



\## Folder Structure



\- data/raw

\- models

\- outputs

\- src



## Project overview ## -day3



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



##  cleaning  ## day-4



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



## Data Quality Report Generation ## -day5



## Objective



The objective of this script is to perform an exploratory assessment of the cleaned polyhouse sensor dataset and automatically generate a data quality report.



## Tasks Performed



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


reports/data\_quality.md


\### Output

The generated report provides a concise overview of data quality and feature distributions, helping validate the dataset before feature engineering, visualization, and machine learning model development.


## Exploratory Data Analysis (EDA) ## -day6

### Objective

Analyze the cleaned polyhouse sensor dataset to understand data distributions, variability, and relationships between environmental conditions and mushroom yield.

### Steps Performed

#### 1. Generated Summary Statistics

Computed descriptive statistics for:

* temperature_c
* humidity_pct
* co2_ppm
* yield_kg

Metrics generated:

* Count
* Mean
* Standard Deviation
* Minimum
* 25th Percentile
* Median
* 75th Percentile
* Maximum

#### 2. Calculated Coefficient of Variation (CV)

Calculated:


CV = Standard Deviation / Mean


Purpose:

* Compare variability across different sensor measurements.
* Identify features with higher relative dispersion.

#### 3. Analyzed Feature Distributions

Compared mean and median values for each feature to determine distribution shape:

* Mean > Median → Right-skewed
* Mean < Median → Left-skewed
* Mean ≈ Median → Approximately symmetric

#### 4. Generated Correlation Matrix

Computed the Pearson correlation matrix for:

* temperature_c
* humidity_pct
* co2_ppm
* yield_kg

Outputs:

reports/correlation_matrix.csv
reports/correlation_matrix.md

Purpose:

* Measure linear relationships between environmental variables and mushroom yield.

#### 5. Created Correlation Heatmap

Generated a heatmap visualization from the correlation matrix.

Output:

reports/figures/corr_heatmap.png

Purpose:

* Visualize positive and negative correlations among features.

#### 6. Created Scatter Plots

Generated scatter plots to examine relationships between yield and environmental conditions:

* Humidity (%) vs Yield (kg)
* Temperature (°C) vs Yield (kg)
* CO₂ (ppm) vs Yield (kg)

Output:

reports/figures/scatter_yield.png

Purpose:

* Identify trends, patterns, and potential outliers.

# # Feature Engineering & Scaling## -day7

## Objective

Prepare machine learning features from the cleaned polyhouse dataset and scale them to a common range using Min-Max Scaling. The resulting feature set will be used for model training in later tasks.

## Input Dataset

Source:

data/interim/02_cleaned.parquet


Target Variable:

yield_kg

## Feature Definitions

### 1. Temperature

Column:

temperature_c

Description:

Average temperature inside the polyhouse in degrees Celsius.

Biological Importance:

Temperature directly affects mushroom growth rate, metabolism, and fruiting body development.

### 2. Humidity

Column:

humidity_pct

Description:

Relative humidity percentage inside the polyhouse.

Biological Importance:

Oyster mushrooms require high humidity for healthy growth and yield production. Low humidity can reduce productivity and affect mushroom quality.

### 3. Carbon Dioxide

Column:

co2_ppm

Description:

Carbon dioxide concentration measured in parts per million (ppm).

Biological Importance:

CO₂ levels influence mushroom respiration and growth conditions. Extremely high or low concentrations may affect yield.

### 4. Temperature–Humidity Interaction Feature

Column:

temp_humid_interaction

Formula:

temp_humid_interaction =
(temperature_c × humidity_pct) / 100

Example:

temperature_c = 25
humidity_pct = 80

temp_humid_interaction =
(25 × 80) / 100
= 20

Biological Importance:

Mushroom growth depends on the combined effect of temperature and humidity rather than either variable independently. This engineered feature helps the model capture interactions between these environmental factors.


## Feature Matrix and Target

Feature Matrix (X):

[
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]


Target Variable (y):

yield_kg

## Scaling Method

Scaler Used:

MinMaxScaler()

Scaling Formula:

x_scaled =
(x - x_min) / (x_max - x_min)

Output Range:

[0, 1]

Purpose:

* Prevents large-scale variables from dominating smaller-scale variables.
* Improves compatibility with many machine learning algorithms.
* Produces comparable feature ranges.

## Saved Outputs

Processed Features:

data/processed/features.parquet


Saved Scaler:

models/minmax_scaler.joblib

## Validation Checks

The following checks are performed after feature engineering:

* Feature and target row counts match.
* No missing values remain after processing.
* All scaled features lie within the range [0, 1].
* Scaler object is successfully saved for future inference.

## Future Improvement

For learning purposes, the scaler is currently fitted on the full cleaned dataset.

 ##chronological Train/Test Split and Feature Scaling## --day8

## Objective

Prepare the cleaned polyhouse sensor dataset for machine learning by:

* Sorting records chronologically
* Creating an 80/20 train-test split
* Preventing data leakage
* Scaling features using MinMaxScaler
* Saving processed datasets and scaler artifacts for future modeling

## Input Dataset

Source file:

data/interim/02_cleaned.parquet

Columns used:

 timestamp     Observation date             
 temperature_c   Temperature in °C            
 humidity_pct  Relative humidity (%)        
 co2_ppm       CO₂ concentration (ppm)      
 yield_kg      Crop yield (target variable) 

## Methodology

### 1. Chronological Sorting

The dataset is sorted by the `timestamp` column before splitting.

df = pd.read_parquet(...).sort_values("timestamp")

This ensures observations remain in time order and future information is not introduced into training data.

### 2. Train/Test Split

An 80/20 chronological split is applied.

split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]


For a dataset containing 365 rows:

Dataset  Rows 
 Train       292  
 Test          73   


### 3. Leakage Verification

The earliest test date must occur after the latest training date.

assert test_start_date > train_end_date

This validation confirms that no future observations are included in the training set.

### 4. Feature Selection

Input features:

temperature_c
humidity_pct
co2_ppm

Target variable:

yield_kg


### 5. Feature Scaling

A MinMaxScaler is fitted only on training data.

scaler.fit(train_features)

Transformation formula:

x_scaled = (x - x_min) / (x_max - x_min)

The fitted scaler is then applied to both train and test datasets.

X_train = scaler.fit_transform(train_features)
X_test = scaler.transform(test_features)

This prevents information from the test set influencing the scaling process.

## Generated Outputs

### Training and Test Datasets

data/processed/train.csv
data/processed/test.csv

### Feature Arrays

data/processed/X_train.npy
data/processed/X_test.npy

### Target Arrays

data/processed/y_train.npy
data/processed/y_test.npy

### Trained Scaler

models/minmax_scaler_train.joblib

## Split Summary

Example output:

Total rows : 365

Train rows : 292
Test rows  : 73

Train Period :
2024-01-01 → 2024-10-18

Test Period :
2024-10-19 → 2024-12-30

Leakage Check Passed 

## Final Deliverables

* Chronological train-test split implemented
* Train and test windows documented
* Leakage validation completed
* MinMaxScaler fitted on training data only
* Scaled feature arrays generated
* Scaler artifact saved for reuse
* Train and test datasets exported
* Modeling-ready arrays created

This stage produces the final modeling datasets (`X_train`, `X_test`, `y_train`, `y_test`) while maintaining strict chronological separation between training and testing periods.

