from src.predict import predict_article

from unittest.mock import Mock

def test_predict_article_passes_text_through_model():

    numeric_features = [0, 1, 0]

    vectorizer = Mock()

    model = Mock()

    vectorizer.transform.return_value = numeric_features

    model.predict.return_value = [True]

    prediction = predict_article(
        "Example article and title text",
        vectorizer,
        model
    )

    vectorizer.transform.assert_called_once_with(
        ["Example article and title text"]
    )

    model.predict.assert_called_once_with(numeric_features)

    assert prediction is True