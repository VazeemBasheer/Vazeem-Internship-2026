from pathlib import Path

Path("reports").mkdir(exist_ok=True)

with open(
    "reports/correlation_matrix.md",
    "w",
    encoding="utf-8"
) as f:
    f.write("# Correlation Matrix\n\n")
    f.write(corr_matrix.to_markdown())