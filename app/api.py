import sys
import os
sys.path.append(os.path.abspath(".."))

from fastapi import APIRouter
from app.schemas import Text, Prediction
from app.model import predict

router = APIRouter()

@router.get('/')
def home():
    return {'message': 'Hello and welcome to SpeechFlowGuard API'}

@router.post('/predict', response_model=Prediction)
def classify(text: Text):
    return predict(text.text)