import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from pathlib import Path
import joblib

# Create output folders
Path("models").mkdir(exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = (
    pd.read_parquet("data/interim/02_cleaned.parquet")
    .sort_values("timestamp")
)

# Engineered feature
df["temp_humid_interaction"] = (
    df["temperature_c"]
    * df["humidity_pct"]
    / 100
)

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

X = df[feature_cols]
y = df["yield_kg"]

# NOTE:
# Fit on full dataset for Task 4 demonstration.
# Will move to train-only fitting on Day 8.
scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

joblib.dump(
    scaler,
    "models/minmax_scaler.joblib"
)

processed = pd.DataFrame(
    X_scaled,
    columns=[f"{c}_scaled" for c in feature_cols]
)

processed["yield_kg"] = y.values

processed.to_parquet(
    "data/processed/features.parquet",
    index=False
)

print("Features saved successfully.")
print(processed.filter(like="_scaled").agg(["min", "max"]))

print(Path("models/minmax_scaler.joblib").exists())

scaler = joblib.load("models/minmax_scaler.joblib")

print(scaler)
print("Minimums:", scaler.data_min_)
print("Maximums:", scaler.data_max_)