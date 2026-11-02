
import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

data_folder = project_root / "data" / "raw"

csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "Please put your CSV file inside data/raw"
    )

for file in csv_files:

    df = pd.read_csv(file)

    print("\nDataset:", file.name)

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nFirst Five Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())
