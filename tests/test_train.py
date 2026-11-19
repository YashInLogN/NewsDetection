import pandas as pd

from src.train import prepare_dataset


def test_prepare_dataset_cleans_rows():
    raw_data = pd.DataFrame({
        "title": [
            "Breaking News",
            " breaking   news ",
            "",
            "Undated story",
        ],
        "text": [
            "First report",
            " first   report ",
            "   ",
            "Article body",
        ],
        "date": [
            "December 31, 2016",
            "December 31, 2016",
            "May 1, 2017",
            "not a date",
        ],
        "label": [False, False, False, True],
    })

    cleaned = prepare_dataset(raw_data)

    assert len(cleaned) == 1
    assert cleaned.iloc[0]["article"] == "Breaking News First report"
    assert cleaned.iloc[0]["year"] == 2016