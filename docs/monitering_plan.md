\# Monitoring Plan



\## Objective



Monitor prediction quality, detect data drift, and identify when retraining is required.



\---



\## Inference Logging



Each prediction request records:



\* UTC Timestamp

\* Temperature (°C)

\* Humidity (%)

\* CO₂ (ppm)

\* Predicted Yield (kg)



Logs are stored in:



```text

logs/predictions.csv

```



No personally identifiable information (PII) is collected.



\---



\## Monitoring Metrics



\### Input Distribution



Track:



\* Average temperature

\* Average humidity

\* Average CO₂



Alert if values move consistently outside historical training ranges.



\### Prediction Monitoring



Monitor:



\* Average predicted yield

\* Maximum predicted yield

\* Prediction frequency



Alert if:



\* Predicted yield exceeds historical maximum by more than 20%

\* Large increases occur without known operational changes



\### Data Quality



Watch for:



\* Missing sensor values

\* Invalid sensor readings

\* Sensor outages



\---



\## Data Drift Scenarios



\### Sensor Calibration Drift



Sensor readings gradually become inaccurate.



Example:



\* Humidity sensor reports values consistently 5% higher than reality.



\### Seasonal Drift



Environmental conditions change significantly from those seen during training.



Example:



\* Monsoon season

\* Extreme summer temperatures



\### Operational Drift



Changes in cultivation practices alter yield relationships.



Example:



\* New substrate formulation

\* Different mushroom variety



\---



\## Retraining Triggers



Retraining should be considered when:



\* New season begins

\* Sensor hardware is replaced

\* Significant operational changes occur

\* Monthly prediction review indicates degraded performance



Recommended retraining frequency:



\* Every 3–6 months

\* Or after collecting substantial new production data



\---



\## Business Monitoring



Track:



\* Forecasted yield vs actual yield

\* Harvest planning efficiency

\* Stockout incidents

\* Wasted harvest trips



Prediction quality should be evaluated using operational outcomes, not only model metrics.



