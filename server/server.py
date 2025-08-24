from flask import Flask, jsonify, request, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # serve frontend

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.getlocations()
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
        'estimated_price': util.get_price(location, sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.loadartifacts()
    app.run(debug=True)
