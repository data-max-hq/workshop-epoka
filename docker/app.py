import pickle
import numpy as np

from flask import Flask, request

app = Flask(__name__)
# Uncomment when model file is available
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello():
    return "Hello"


# https://medium.com/analytics-vidhya/create-your-first-ml-web-app-with-flask-ed0c4bb54312
# Refactor when model file is available
@app.route('/predict', methods=['POST'])
def predict():
    json = request.json
    # int_features = [float(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    return json
