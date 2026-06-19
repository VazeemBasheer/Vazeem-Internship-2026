# Capstone Reflection — Mushroom Yield Forecast

*Draft starting point — personalize this in your own words before submitting.*

Over the past 22 days I went from a raw CSV of polyhouse sensor readings to a deployed, monitored machine learning application — and the gap between "a model that scores well" and "a model a grower can actually trust" turned out to be the real lesson of this capstone.

## Top 3 Skills Learned

1. **Leakage-safe validation for time series.** Building the chronological 80/20 split, asserting `test\_start\_date > train\_end\_date`, and fitting the scaler only on training data taught me that a random train/test split can quietly inflate scores on sensor data where adjacent days are correlated — and that the fix has to be enforced in code, not just remembered.
2. **Disciplined model comparison.** Running Linear Regression against a default and a tuned Random Forest, with a pre-agreed tie-breaking rule (prefer the simpler model within 0.05 kg MAE), meant champion selection wasn't a judgment call made after the fact. It also showed me that added complexity (Random Forest) doesn't automatically win.
3. **End-to-end deployment thinking.** Going from a `predict.py` module to a Streamlit dashboard to a verified cloud deployment — and designing a monitoring plan before anything had actually drifted — changed how I think about a model: not a notebook result, but infrastructure with a lifecycle.

## 2 Areas to Grow

1. **Earlier testing.** My pytest suite and CLI/dashboard consistency checks landed around Day 18, near the end of the pipeline. Writing even a few tests for `clean.py` and `split\_scale.py` back on Days 4–8 would have caught issues closer to the source.
2. **Richer feature engineering.** The temperature × humidity interaction term didn't beat the raw features, and the report's own limitations flag missing variables — light intensity, airflow, substrate moisture. With more time I'd explore lag features (yesterday's conditions predicting today's yield) and bring in those additional sensor types.

If I had to redo one thing, it would be moving leakage checks and basic tests earlier in the pipeline instead of treating them as a late-stage validation step.

