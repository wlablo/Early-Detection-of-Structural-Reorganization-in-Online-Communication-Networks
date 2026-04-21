from pathlib import Path
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[1]

print("IRA samples:")
for path in sorted((REPO_ROOT / "data" / "samples" / "ira").glob("*.csv")):
    df = pd.read_csv(path, nrows=5)
    print(f"- {path.name}: {len(df.columns)} columns")

brexit_path = REPO_ROOT / "data" / "samples" / "brexit" / "tcat_brexit_train_sample.csv"
brexit_df = pd.read_csv(brexit_path, sep=';', decimal=',', nrows=5)
print(f"Brexit sample columns: {len(brexit_df.columns)}")
