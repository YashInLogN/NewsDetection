from pathlib import Path
import joblib
import streamlit as st
from src.predict import predict_article

st.title("News Detection Working Model")

st.info(
    "Paste a new article here to find the prediction of the model."
)

article_text = st.text_area(
    "News article",
    placeholder= "Enter the article here",
    height=250
)

@st.cache_resource
def load_model_objects():
    root_path = Path(__file__).resolve().parent
    model_path = root_path / "models" / "news_detection.joblib"

    saved_objects = joblib.load(model_path)

    return saved_objects["vectorizer"], saved_objects["model"]

if st.button("analyze article"):
    if not article_text.strip():
        st.warning("Paste the article in the placeholder")
    else:
        vector, model = load_model_objects()
        prediction = predict_article(article_text, vector, model)

        if prediction:
            st.success("Model prediction: True (labeled real in the dataset)")
        else:
            st.warning("Model prediction: False (labeled fake in the dataset)")
    


