from PIL import Image
import numpy as np
from io import BytesIO
from tensorflow import keras
import config

def make_prediction(image: bytes):
    img = Image.open(BytesIO(image))
    img = img.resize((135, 135))
    X = np.array([np.array(img)])
    model = keras.models.load_model(config.MODEL_PATH)
    prediction = model.predict(X)
    res = prediction[0][0]
    return res