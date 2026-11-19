# newsDetection

An educational NLP and machine learning project that classifies news articles using the labels in the ISOT Fake News Dataset. The current training script uses word counts and Logistic Regression. This is a learning prototype, not a fact-checking service.

## What it does

- Combines each article's headline and body into one text input.
- Removes empty articles and duplicate article text before splitting the data.
- Trains on dated articles from 2015–2016 and evaluates on 2017 articles.
- Converts text into word-count features with `CountVectorizer`.
- Trains a Logistic Regression classifier and reports accuracy, precision, recall, and F1.
- Saves the fitted vectorizer and classifier together so predictions use the same vocabulary.

The date split tests whether the model can classify later articles from this dataset. It does not establish that the model can identify false claims in current news. The class balance changes substantially between the training and test periods, and the dataset's labels are tied to different source groups.

## Dataset

This project uses the [ISOT Fake News Dataset](https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/fake-news-detection-datasets/) from the Information Security and Object Technology (ISOT) Research Group at the University of Victoria. The original files are `Fake.csv` and `True.csv`; the project uses a combined CSV named `fake_news_labeled.csv`.

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

## Getting started

Use Python 3.10 or later. From the project root, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the listed dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Train and evaluate

From the project root, run:

```bash
python src/train.py
```

The script prints the training and test metrics, then saves the fitted CountVectorizer and Logistic Regression model to `models/news_detection.joblib`.

## Make a prediction

`src/predict.py` loads the saved vectorizer and classifier. Replace the example text in its `test_article` variable with a headline and article body, then run:

```bash
python src/predict.py
```

The output is the model's predicted dataset label (`True` or `False`). It is a prediction based on learned patterns, not evidence that a claim is factually true or false.

## Project structure

```text
newsdetection/
├── data/                  # Local combined dataset; excluded from Git
├── models/                # Saved model artifacts
├── notebooks/             # Data exploration and experiments
├── src/
│   ├── train.py           # Prepare data, train, evaluate, and save
│   └── predict.py         # Load saved artifacts and predict a label
├── .gitignore
├── README.md
└── requirements.txt
```

## Limitations and responsible use

- The dataset is historical and largely focused on English-language political and world news.
- The label groups come from different source collections, so a model can learn source or writing-style cues instead of claim veracity.
- A time-based result on this dataset does not measure performance on current articles or unseen publishers.
- Do not use this model as the sole basis for moderating, ranking, or labeling real-world news.
- Check source terms and copyright before sharing the data or using it commercially.

## Citation

If you use this dataset in academic work, cite the papers listed in the [official dataset description](https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/02/ISOT_Fake_News_Dataset_ReadMe.pdf):

> Ahmed, H., Traore, I., & Saad, S. (2018). “Detecting opinion spams and fake news using text classification.” *Journal of Security and Privacy*, 1(1).

> Ahmed, H., Traore, I., & Saad, S. (2017). “Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques.” In *Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments*, Lecture Notes in Computer Science, vol. 10618, pp. 127–138.

## License

No license has been selected for this repository yet. Add a `LICENSE` file before inviting reuse or accepting contributions. Dataset reuse and redistribution may have separate terms from the project code.
