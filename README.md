# newsDetection

An educational machine learning project for classifying news article text as **true** or **false** using natural language processing (NLP). The project starts with a TF-IDF and Logistic Regression baseline, then can be extended with other models and evaluation methods.

> **Important:** This is a research and learning project. A model trained on this dataset cannot reliably determine whether current news is true. It may learn writing style, topic, publisher, or time-period patterns instead of checking claims against evidence.

## Dataset

This project uses the [ISOT Fake News Dataset](https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/fake-news-detection-datasets/), published by the Information Security and Object Technology (ISOT) Research Group at the University of Victoria. The original release contains two CSV files, `Fake.csv` and `True.csv`. The combined version adds a `label` column:

| Label | Meaning | Rows |
| --- | --- | ---: |
| `false` | Article came from the dataset's fake-news collection | 23,481 |
| `true` | Article came from the dataset's Reuters collection | 21,417 |
| **Total** |  | **44,898** |

The dataset documentation says the truthful articles were collected from Reuters and the fake articles from outlets identified as unreliable by PolitiFact and Wikipedia. Most examples focus on politics and world news and were collected mainly from 2016–2017. Labels describe the dataset's source-based categories; they are not independent fact-checks of every claim in each article.

### Columns

| Column | Description |
| --- | --- |
| `title` | Article headline |
| `text` | Article body |
| `subject` | Dataset topic/category |
| `date` | Article publication date as supplied in the source data |
| `label` | Target class: `false` or `true` |

Place the combined CSV at `data/fake_news_labeled.csv` when running the project locally. Keep the dataset out of Git if the file is too large or if you have not confirmed the terms for redistributing it. Download the original files from the [ISOT dataset page](https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/fake-news-detection-datasets/) and combine them with labels if needed.

## Project workflow

1. Inspect and clean the article text; check missing values, duplicates, and label balance.
2. Split data into training and test sets before fitting preprocessing steps.
3. Convert text to numeric features with TF-IDF.
4. Train a baseline classifier such as Logistic Regression or Linear SVM.
5. Evaluate with precision, recall, F1 score, and a confusion matrix—not accuracy alone.
6. Review misclassified articles and compare alternative models.

For a stronger evaluation, check for duplicate or near-duplicate stories and consider a time-based or source-aware split. Randomly splitting this dataset can make performance look better than it will be on newer articles because the examples are old and their sources and topics may correlate with labels.

## Getting started

Recommended environment: Python 3.10 or later.

```bash
git clone <your-repository-url>
cd newsDetection
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the initial project dependencies:

```bash
python -m pip install --upgrade pip
pip install pandas scikit-learn joblib
```

Put `fake_news_labeled.csv` in the `data/` directory. Model training and prediction commands will be added as the project is built.

## Suggested repository structure

```text
newsDetection/
├── data/                  # Local dataset; usually excluded from Git
├── models/                # Saved model artifacts (optional)
├── notebooks/             # Exploration and experiments
├── src/                   # Data preparation, training, and prediction code
├── .gitignore
├── README.md
└── requirements.txt
```

## Responsible use and limitations

- Treat predictions as experimental signals, not proof that an article is true or false.
- The dataset is historical, largely English-language, and strongly centered on US politics and world news.
- Since the two classes came from different source groups, a model may learn publisher or style cues rather than factual accuracy.
- Check dataset terms and source copyright before redistributing the data or using it commercially. The dataset page provides the download and description; consult its associated papers when using it in research.
- Do not use this model as the sole basis for moderating, ranking, or labeling real-world news.

## Citation

If you use the dataset in academic work, cite the dataset authors' papers:

> Ahmed, H., Traore, I., & Saad, S. (2018). “Detecting opinion spams and fake news using text classification.” *Journal of Security and Privacy*, 1(1).

> Ahmed, H., Traore, I., & Saad, S. (2017). “Detection of Online Fake News Using N-Gram Analysis and Machine Learning Techniques.” In *Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments*, Lecture Notes in Computer Science, vol. 10618, pp. 127–138.

See the [official dataset description](https://onlineacademiccommunity.uvic.ca/isot/wp-content/uploads/sites/7295/2023/02/ISOT_Fake_News_Dataset_ReadMe.pdf) for the dataset details and full citation information.

## License

No project license has been selected yet. Add a `LICENSE` file before inviting reuse or accepting contributions. Dataset reuse and redistribution may have separate terms from this repository's code; verify the original source terms first.
