from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "fake_news_labeled.csv"
df = pd.read_csv(data_path)

print(df.head())

