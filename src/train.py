from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score
from pathlib import Path
import pandas as pd
import joblib

project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "data" / "fake_news_labeled.csv"
df = pd.read_csv(data_path)

#print(df.head())

#print(df.columns)

print("Rows before cleanup: ", df.shape[0])

df["article"] = (
    df["title"].fillna("").astype(str) + " " +
    df["text"].fillna("").astype(str)
).str.strip()

df = df[df["article"] != ""].copy()

df["article_key"] = df["article"].str.lower().str.replace(r"s\+", " ", regex=True).str.strip()

df = df.drop_duplicates(subset="article_key").copy()

print("Rows after cleanup: ", df.shape[0])

print(df["date"].head())

df["date_parsed"] = pd.to_datetime(
    df["date"],
    format="mixed",
    errors="coerce"
)

print(df[["date", "date_parsed"]].head())

df["year"] = df["date_parsed"].dt.year

print(df[["date_parsed", "year"]].head())

dated_df = df[df["date_parsed"].notna()].copy()

train_df = df[df["year"] <= 2016]

test_df = df[df["year"] == 2017]

#print(df["year"].value_counts(normalize=True) * 100)

X_train = train_df["article"]

y_train = train_df["label"]

X_test = test_df["article"]

y_test = test_df["label"]

count_vector = CountVectorizer(max_features=5000)

X_train_count = count_vector.fit_transform(X_train)
X_test_count = count_vector.transform(X_test)

model = LogisticRegression(max_iter=5000)

model.fit(X_train_count, y_train)

y_pred = model.predict(X_test_count)

train_accuracy = model.score(X_train_count, y_train)
test_accuracy = model.score(X_test_count, y_test)

print("Train accuracy: ", train_accuracy)
print("Test accuracy: ", test_accuracy)


precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)


print("Precision: ", precision)
print("Recall: ", recall)
print("f1: ", f1)


error = pd.DataFrame({
    "article": X_test.reset_index(drop=True),
    "actual": y_test.reset_index(drop=True),
    "predicted": y_pred
})

print(error[["actual", "predicted"]].head())

print(error[error["predicted"] != error["actual"]].shape)

model_path = project_root / "models" / "news_detection.joblib"

model_path.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(
    {"vectorizer": count_vector, "model": model},
    model_path
)

print("Saved model to: ", model_path)