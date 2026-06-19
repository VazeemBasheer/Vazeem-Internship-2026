# Mushroom Yield Forecast

## Zelbytes Agritech Capstone — Final Presentation

*Presenter: Vazeem | Day 22 of 22*

\---

## Agenda

* The agritech problem
* Data pipeline \& EDA
* Modeling \& validation strategy
* Results \& champion model
* Live demo
* Lessons learned \& next steps
* Q\&A

\---

## Problem

* Predict daily oyster mushroom yield (kg) from polyhouse sensors
* Inputs: Temperature (°C), Humidity (%), CO₂ (ppm)
* Today's reality: reactive harvest planning → stockouts, waste, inefficient labor/transport
* Goal: give growers a forecast they can act on, plus levers to adjust conditions

\---

## Data Pipeline

**Ingest → Clean → EDA → Feature Engineering → Model**

* 365 daily records (Jan 1 – Dec 30, 2024), 0 missing values, 0 duplicates
* Range validation: Temp 10–35°C · Humidity 50–100% · CO₂ 400–2000 ppm
* Forward-fill imputation for short sensor gaps (max 2 days)

\---

## EDA Highlights

|Sensor|Correlation with Yield|
|-|-|
|Temperature|r = 0.524 (moderate +)|
|Humidity|r = 0.242 (weak +)|
|CO₂|r = −0.260 (weak −)|

Near-zero collinearity between sensors → model coefficients stay interpretable.

\---

## Validation Strategy

* **Chronological 80/20 split** — train: Jan 1–Oct 18, test: Oct 19–Dec 30
* `assert test\_start\_date > train\_end\_date` — hard guardrail against leakage
* Scaler fit on **training data only**, then applied to test
* `TimeSeriesSplit` used for cross-validation and hyperparameter tuning

\---

## Model Results

|Model|CV MAE (kg)|Test MAE (kg)|Test R²|
|-|-|-|-|
|**Linear Regression (Champion)**|**0.441**|**0.419**|**0.427**|
|Random Forest (Tuned)|0.466|0.445|0.369|
|Random Forest (Default)|0.475|0.450|0.327|

\---

## Why Linear Regression Won

* Lowest Test MAE, lowest RMSE, highest R² on unseen data
* **Tie-break rule:** prefer the simpler model if Δ Test MAE < 0.05 kg

  * RF Tuned − Linear = 0.026 kg → rule favors Linear
* Default RF overfit: Train MAE 0.167 kg vs Test MAE 0.450 kg
* Transparent coefficients (Temp +1.894, Humidity +0.959, CO₂ −1.213) stakeholders can trust

\---

## Live Demo

[**Streamlit App →**](https://vazeem-internship-2026-5yryfkqukyvqh9zgefpj7z.streamlit.app/)

Example: Temp 22°C, Humidity 88%, CO₂ 920 ppm → **Estimated Yield: 17.00 kg**

*(Backup screenshot ready in case of connectivity issues)*

\---

## Lessons \& Next Steps

**Lessons learned**

* Data leakage is sneaky in time-series data — chronological splits are non-negotiable
* Simpler isn't automatically worse: Linear Regression beat a tuned Random Forest here
* Testing and leakage checks should start on Day 1, not Day 8

**Next steps**

* Add sensors: light intensity, airflow, substrate moisture
* Automate retraining every 3–6 months or after sensor/operational changes
* Build a drift-detection dashboard

\---

## Anticipated Q\&A

**Data leakage?** Chronological split + assertion + scaler fit on train only. Random K-fold would leak because adjacent days are highly correlated.

**Why MAE?** Interpretable in kilograms for growers; RMSE and R² reported alongside for the full picture.

**Deployment failure modes?** Out-of-range inputs (flagged with warnings), sensor calibration drift, cloud/local mismatch (verified identical predictions).

\---

## Thank You

* Mentors \& peers for feedback across all 22 days
* Built with: pandas, NumPy, scikit-learn, matplotlib, joblib, pyarrow, Streamlit, pytest
* Questions welcome!

