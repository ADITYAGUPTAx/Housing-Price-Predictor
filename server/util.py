import json
import pickle
import os
import pandas as pd
import numpy as np

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

    # Get base directory of this file
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define paths relative to this file
    columns_path = os.path.join(base_dir, "artifacts", "columns.json")
    model_path = os.path.join(base_dir, "artifacts", "model.pickle")

    # Load columns
    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    # Load model
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully")

if __name__ == "__main__":
    loadartifacts()
