from pathlib import Path
import joblib

root_path = Path(__file__).resolve().parents[1]

model_path = root_path / "models" / "news_detection.joblib"

saved_objects = joblib.load(model_path)

vector = saved_objects["vectorizer"]
model = saved_objects["model"]