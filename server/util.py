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

if __name__ == "__main__":
    loadartifacts()
    print(getlocations())
    print(get_price("yelenahalli", 2000, 3, 2))
