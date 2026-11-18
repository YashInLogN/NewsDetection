from pathlib import Path
import joblib

root_path = Path(__file__).resolve().parents[1]

model_path = root_path / "models" / "news_detection.joblib"

saved_objects = joblib.load(model_path)

vectorizer = saved_objects["vectorizer"]
model = saved_objects["model"]

def predict_article(article_text):
    article_features = vectorizer.transform([article_text])
    model_prediction = model.predict(article_features)[0]
    return model_prediction

test_article = "hello, there"
model_pred = predict_article(test_article)
print(model_pred)