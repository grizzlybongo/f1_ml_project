from pathlib import Path
import pandas as pd

folder = Path("C:/Users/idris/f1_analysis")

for file in folder.glob("*.csv"):
    df = pd.read_csv(file, nrows=0)

    print(f"\nFile: {file.name}")
    print("Headers:", list(df.columns))