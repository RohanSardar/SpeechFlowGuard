import sys
import os
sys.path.append(os.path.abspath(".."))

from fastapi import FastAPI
from app.api import router

app = FastAPI(title="SpeechFlowGuard")

app.include_router(router)
