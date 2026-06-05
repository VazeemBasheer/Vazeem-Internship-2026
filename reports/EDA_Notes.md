# EDA Notes

## Objective

Perform exploratory data analysis on the cleaned polyhouse sensor dataset to understand data distribution, variability, and relationships between environmental factors and mushroom yield.

## Dataset

* Source: `02_cleaned.parquet`
* Features analyzed:

  * temperature_c
  * humidity_pct
  * co2_ppm
  * yield_kg

## Summary Statistics

Summary statistics were generated using the `describe()` function for all numerical features.

Metrics reviewed:

* Count
* Mean
* Standard Deviation
* Minimum
* 25th Percentile
* Median (50th Percentile)
* 75th Percentile
* Maximum

## Variability Analysis

The coefficient of variation (CV = standard deviation / mean) was calculated for each feature.

Purpose:

* Compare variability across measurements with different units.
* Identify features with relatively high or low dispersion.

Observations:

* Features with lower CV values are more stable.
* Features with higher CV values exhibit greater relative variation.

## Distribution Analysis

Mean and median values were compared for each feature.

Interpretation:

* Mean > Median → slight right-skewed distribution.
* Mean < Median → slight left-skewed distribution.
* Mean ≈ Median → approximately symmetric distribution.

The generated report documents the skew direction for:

* temperature_c
* humidity_pct
* co2_ppm
* yield_kg

## Correlation Analysis

A Pearson correlation matrix was computed for:

* temperature_c
* humidity_pct
* co2_ppm
* yield_kg

Outputs:

* `reports/correlation_matrix.csv`
* `reports/correlation_matrix.md`
* `reports/figures/corr_heatmap.png`

Purpose:

* Measure linear relationships between sensor variables and yield.
* Identify potentially useful predictors for future modeling.

## Scatter Plot Analysis

Scatter plots were generated for:

1. Humidity (%) vs Yield (kg)
2. Temperature (°C) vs Yield (kg)
3. CO₂ (ppm) vs Yield (kg)

Output:

* `reports/figures/scatter_yield.png`

Purpose:

* Visualize relationships between environmental conditions and mushroom yield.
* Identify trends, clusters, and potential outliers.

## Conclusion

The EDA process successfully generated descriptive statistics, variability measures, distribution insights, correlation analysis, and visualizations. These outputs provide a foundation for feature selection, predictive modeling, and further analysis of mushroom yield in controlled polyhouse environments.
