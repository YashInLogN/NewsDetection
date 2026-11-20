# News Detection

An educational NLP and machine learning project that classifies news articles using labels from the ISOT Fake News Dataset. It uses word-count features and Logistic Regression, and includes a Streamlit interface for trying the saved model.

This is a learning project, not a fact-checking service. A prediction reflects patterns the model learned from this dataset; it does not prove whether a claim is true or false.

## What the project does

- Combines each article's headline and body into one text input.
- Removes empty articles and duplicate article text.
- Uses a time-based split: articles dated through 2016 for training and 2017 articles for testing.
- Converts text into word-count features with `CountVectorizer`.
- Trains a Logistic Regression classifier and reports accuracy, precision, recall, and F1.
- Saves the fitted vectorizer and classifier together in `models/news_detection.joblib`.
- Provides a Streamlit app where a user can paste article text and view the model's dataset-label prediction.
- Runs the test suite automatically on pushes and pull requests with GitHub Actions.

The time-based evaluation checks performance on later articles from this dataset. It does not establish performance on current news or on articles from unseen publishers. The label balance changes substantially between training and test periods, and the labels are tied to different source groups.

## Dataset

This project uses the [ISOT Fake News Dataset](https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/fake-news-detection-datasets/) from the Information Security and Object Technology (ISOT) Research Group at the University of Victoria. The original files are `Fake.csv` and `True.csv`; this project uses a combined CSV named `fake_news_labeled.csv`.

The original dataset contains 44,898 articles:

| Label | Dataset meaning | Articles |
| --- | --- | ---: |
| `False` | Article from the dataset's fake-news collection | 23,481 |
| `True` | Article from the dataset's Reuters collection | 21,417 |

The combined file has these columns:

| Column | Description |
| --- | --- |
| `title` | Article headline |
| `text` | Article body |
| `subject` | Dataset topic or category |
| `date` | Publication date as supplied by the source |
| `label` | Target label: `False` or `True` |

The dataset documentation says truthful articles were collected from Reuters and fake articles from outlets identified as unreliable by PolitiFact and Wikipedia. Most examples focus on politics and world news, and the articles were collected mainly from 2016–2017. Labels reflect the dataset's collection and source categories; they are not independent fact-checks of every claim.

Place the combined CSV at `data/fake_news_labeled.csv`. The dataset is excluded from Git by the repository's ignore rule. Check the original dataset terms before redistributing it or using it commercially.

## Requirements and setup

Use Python 3.12 to match the version used by the CI workflow. From the project root, create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development and running tests, install the development dependencies too:

```bash
python -m pip install -r requirements-dev.txt
```

## Train and evaluate the model

Make sure `data/fake_news_labeled.csv` is in place, then run:

```bash
python src/train.py
```

The script prints the training and test metrics, then creates `models/news_detection.joblib`. The Streamlit app needs this saved model, so train the model before launching the app if the artifact is not present.

## Run the Streamlit app

From the project root, run:

```bash
python -m streamlit run app.py
```

Paste an article into the text area and click **Analyze article**. The app reports `True` or `False`, matching the labels used in this dataset (`True` is the Reuters collection and `False` is the fake-news collection). These are model predictions, not verified facts.

## Run tests

With the development dependencies installed, run:

```bash
python -m pytest -q
```

GitHub Actions runs this command automatically whenever code is pushed or a pull request is opened. Check the repository's **Actions** tab to see whether a workflow run passed.

## Make a prediction from Python

`src/predict.py` contains the `predict_article(article_text, vectorizer, model)` helper and a small standalone example. After training, run:

```bash
python src/predict.py
```

The helper accepts the fitted vectorizer and model explicitly, transforms the input text using the saved vocabulary, and returns a predicted dataset label.

## Project structure

```text
newsdetection/
├── .github/
│   └── workflows/
│       └── tests.yml        # Run tests on pushes and pull requests
├── data/                   # Local combined dataset; excluded from Git
├── models/                 # Saved model artifact created by training
├── notebooks/              # Data exploration and experiments
├── src/
│   ├── train.py            # Prepare data, train, evaluate, and save
│   └── predict.py          # Prediction helper and standalone example
├── tests/                  # Automated tests
├── app.py                  # Streamlit user interface
├── requirements.txt        # Runtime dependencies
├── requirements-dev.txt    # Test/development dependencies
└── README.md
```

## Limitations and responsible use

- The dataset is historical and largely focused on English-language political and world news.
- The label groups come from different source collections, so the model can learn source or writing-style cues instead of claim veracity.
- A time-based result on this dataset does not measure performance on current articles or unseen publishers.
- Do not use this model as the sole basis for moderating, ranking, or labeling real-world news.
- Check source terms and copyright before sharing the data or using it commercially.

## Citation

If you use this dataset in academic work, cite the papers listed in the [official dataset description](https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/02/ISOT_Fake_News_Dataset_ReadMe.pdf):

> Ahmed, H., Traore, I., & Saad, S. (2018). “Detecting opinion spams and fake news using text classification.” *Journal of Security and Privacy*, 1(1).

> Ahmed, H., Traore, I., & Saad, S. (2017). “Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques.” In *Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments*, Lecture Notes in Computer Science, vol. 10618, pp. 127–138.

## License

No license has been selected for this repository yet. Add a `LICENSE` file before inviting reuse or accepting contributions. Dataset reuse and redistribution may have separate terms from the project code.
