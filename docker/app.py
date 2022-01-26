import pickle
import numpy as np
import logging

from flask import Flask, request

logging.basicConfig(level=logging.INFO)

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def hello():
    logging.info(f"Received request.")
    return "Hello"


# https://medium.com/analytics-vidhya/create-your-first-ml-web-app-with-flask-ed0c4bb54312
# Refactor when model file is available
@app.route('/predict', methods=['POST'])
def predict():
    features = list(request.json.values())
    logging.info(f"Received json: {features}")

    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    return { "quality": prediction[0] }
