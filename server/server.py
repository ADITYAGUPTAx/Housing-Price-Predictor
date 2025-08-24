from flask import Flask, jsonify, request, render_template

import json
import pickle
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_price(location, sqft, bhk, bath):
   
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    # Create input array with correct dtype
    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = sqft
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1

    # Do NOT force dtype=int, keep as float
    x_df = pd.DataFrame([x], columns=__data_columns, dtype=float)
    return round(__model.predict(x_df)[0], 2)


def getlocations():
    loadartifacts()
    return __locations

def loadartifacts():
    global __locations, __data_columns, __model
    print("Loading artifacts......")
    with open("C:\\Users\\aditya\\Documents\\Bangalore housing price predictor\\server\\artifacts\\columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    with open("C:\\Users\\aditya\\Documents\\Bangalore housing price predictor\\server\\artifacts\\model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("Artifacts loaded successfully")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # serve frontend

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations':getlocations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    location = data['location']
    sqft = float(data['sqft'])
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price':get_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
   loadartifacts()
   app.run(debug=True)
