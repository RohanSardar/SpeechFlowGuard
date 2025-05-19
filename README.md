# SpeechFlowGuard

A machine learning web API that detects toxic language in user comments using classical ML models (TF-IDF + Logistic Regression). Built with **FastAPI**, trained on the **Jigsaw Toxic Comment Classification Challenge** dataset.

## ✅ Features

- Multi-label classification: 
  - `toxic`, `severe_toxic`, `obscene`, `threat`, `insult`, `identity_hate`
- Real-time REST API (FastAPI)
- Modular codebase
- Dockerized for portability
- Preprocessed with custom regex cleaner


## 🧪 Model Details

- Vectorizer: `TfidfVectorizer` (max_features=4096, stop_words='english')
- Classifier: `LogisticRegression` (class_weight='balanced', max_iter=500, C=1.6)
- Trained on: [Jigsaw Toxic Comment Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## 🗂️ Project Structure

```
SpeechFlowGuard/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── model.py
│   ├── schemas.py
│   ├── utils.py
│   └── config.py
├── data/
│   ├── data_processed.csv
│   └── trains.csv
├── models/
│   ├── tf-idf_vectorizer.pkl
│   └── classifier.pkl
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── tf-idf_model_train.ipynb
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## 🧰 Technical Stack
- **Language:** Python 3.12+
- **Framework:** FastAPI (ASGI-compatible)
- **ML Model:**
    - TfidfVectorizer for feature extraction
    - LogisticRegression (one classifier per label, binary relevance method)
- **Serialization:** `dill` for saving sklearn models
- **Request Schema:** Pydantic-based input validation
- **Serving:** Uvicorn for ASGI serving
- **Containerization:** Docker 

## 📡 API Endpoints
The FastAPI server exposes the following endpoints:

### `GET /`

Returns a welcome message to confirm the API is live.

**Request:**

`curl http://localhost:8000/`

**Response:**
```
{
  "message": "Hello and welcome to SpeechFlowGuard API"
}
```
### `POST /predict`

Performs multi-label classification on the input text and returns the predicted probabilities for each toxicity label.

**Request:**
```
POST /predict
Content-Type: application/json
```
**Request Body:**
```
{
  "text": "You are a criminal person"
}
```
**Response:**
```
{
  "toxic": 0.6774,
  "severe_toxic": 0.039,
  "obscene": 0.0994,
  "threat": 0.1204,
  "insult": 0.5151,
  "identity_hate": 0.6681
}
```

## 🛠️ Git Setup & Repository Cloning
If you haven't installed Git:

### 🔨 Install Git
**Windows:**

Download from https://git-scm.com/download/win and install with default settings.

**Ubuntu/Linux:**
```
sudo apt update
sudo apt install git
```

**macOS:**
```
brew install git
```

### 📦 Clone the Repository
```
git clone https://github.com/your-username/SpeechFlowGuard.git
cd SpeechFlowGuard
```

## 🔧 How to Train the Model

Use the Jupyter notebooks in `notebooks/` or create a script to:

1. Load and preprocess the dataset.
2. Train TF-IDF and LogisticRegression models.
3. Save them using `dill`.

## 🐳 Docker Setup
🔥 1. Build the Image
```
docker build -t speechflowguard .
```
🚀 2. Run the Container
```
docker run -p 8000:8000 speechflowguard
```
You can also access the interactive API docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**Example using cURL**
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "You are a criminal person"}'
```

**Response**
```
{
  "toxic": 0.6774,
  "severe_toxic": 0.039,
  "obscene": 0.0994,
  "threat": 0.1204,
  "insult": 0.5151,
  "identity_hate": 0.6681
}
```

