import sys
import os
sys.path.append(os.path.abspath(".."))

import dill
from app.config import MODEL_PATH, VECTORIZER_PATH, LABELS
from sklearn.base import BaseEstimator

with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = dill.load(f)
with open(MODEL_PATH, 'rb') as f:
    models: dict[str, BaseEstimator] = dill.load(f)

def predict(text: str) -> dict:
    X = vectorizer.transform([text])
    result = {}
    for label in LABELS:
        model = models[label]
        pred = model.predict_proba(X)[0][1]
        result[label] = round(float(pred), 4)
    return result