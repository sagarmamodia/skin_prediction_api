from fastapi import FastAPI, Form, UploadFile, Request, File
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated, Union
import os
from fastapi.templating import Jinja2Templates
import config
from schemas import PredictionResponse
from ml_processing import make_prediction

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

templates = Jinja2Templates(directory=config.TEMPLATES_PATH)

@app.get('/')
def index(request:Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.post('/predict')
def predict(request:Request, image: UploadFile):

    res = make_prediction(image.file.read())

    return templates.TemplateResponse(
        request=request, name="prediction.html", context={"prediction": int(res)}
    )

@app.post('/api/predict', response_model=PredictionResponse)
def api_predict(image: UploadFile):
    res = make_prediction(image.file.read())
    return {"prediction": res}
