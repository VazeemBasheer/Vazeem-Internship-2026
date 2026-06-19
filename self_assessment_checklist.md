# Self-Assessment Checklist — Mushroom Yield Forecast

**Zelbytes Agritech Capstone | Days 1–22**

Pre-filled based on evidence in your README and report — review honestly and adjust anything that doesn't match how it actually went.

## Phase 1 — Foundations \& Ingestion (Days 1–3)

* \[x] **Day 1:** Set up venv, installed dependencies (pandas, numpy, matplotlib, scikit-learn, jupyter), ran smoke test
* \[x] **Day 2:** Defined project structure (`data/raw`, `models`, `outputs`, `src`) and project overview
* \[x] **Day 3:** Built `ingest.py` — raw sensor CSV → `01\_loaded.parquet`

## Phase 2 — Cleaning, Quality \& EDA (Days 4–7)

* \[x] **Day 4:** `clean.py` — missing-value check, range validation, forward-fill imputation (max 2-day gap), deduplication
* \[x] **Day 5:** Automated data quality report (summary stats, skew, coefficient of variation)
* \[x] **Day 6:** Full EDA — correlation matrix, heatmap, scatter plots vs. yield
* \[x] **Day 7:** Feature engineering \& MinMax scaling; tested temp × humidity interaction term (dropped — didn't improve CV stability)

## Phase 3 — Modeling \& Validation (Days 8–14)

* \[x] **Day 8:** Chronological 80/20 split with leakage assertion; scaler fit on training data only
* \[x] **Day 9:** Baseline Linear Regression trained and evaluated (MAE/RMSE/R²)
* \[x] **Day 10:** Residual diagnostics — no major bias or heteroscedasticity found
* \[x] **Day 11:** Default Random Forest trained + feature importance analysis
* \[x] **Day 12:** `TimeSeriesSplit` cross-validation; checked train/test gap for overfitting
* \[x] **Day 13:** Hyperparameter tuning via `GridSearchCV` (27 combinations × 3 folds)
* \[x] **Day 14:** Compared all 3 models; selected Linear Regression as champion via the tie-break rule

## Phase 4 — Inference \& Deployment (Days 15–19)

* \[x] **Day 15:** Built `predict.py` inference module + Python API
* \[x] **Day 16:** Basic Streamlit app — sliders + prediction
* \[x] **Day 17:** Enhanced dashboard — what-if sensitivity chart, metadata \& methodology expanders
* \[x] **Day 18:** Validated CLI vs. dashboard outputs match; pytest suite passing
* \[x] **Day 19:** Deployed to Streamlit Community Cloud; verified cloud predictions match local

## Phase 5 — Monitoring \& Wrap-Up (Days 20–22)

* \[x] **Day 20:** Monitoring plan defined — inference logging, drift scenarios, retraining triggers
* \[ ] **Day 21:** ⚠️ Not explicitly logged in your README — likely report write-up, testing, and repo polish. Confirm and check off once verified.
* \[ ] **Day 22 (today):** Capstone presentation, self-assessment, reflection, final submission

\---

## Confidence Self-Rating

Be honest — this is for your own growth tracking, not for your mentor.

|Area|Confidence (1–5)|
|-|-|
|Data cleaning \& validation|5|
|EDA \& statistical reasoning|5|
|Leakage-safe ML validation|4|
|Model comparison \& selection|3|
|Deployment \& monitoring|5|

## If Asked "What Would You Redo?"

Two strong, evidence-backed answers from your own project:

1. **Earlier testing** — the pytest suite and CLI/dashboard consistency checks landed on Day 18, near the end.
2. **Stricter leakage discipline from Day 1** — the chronological-split safeguards didn't arrive until Day 8.

