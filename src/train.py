from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "fake_news_labeled.csv"
df = pd.read_csv(data_path)

print(df.head())

print(df.columns)

df["article"] = (
    df["title"].fillna("").astype(str) + " " +
    df["text"].fillna("").astype(str)
).str.strip()

df = df[df["article"] != ""].copy()

df["article_key"] = df["article"].str.lower().str.replace(r"s\+", " ", regex=True).str.strip()

df = df.drop_duplicates(subset="article_key").copy()