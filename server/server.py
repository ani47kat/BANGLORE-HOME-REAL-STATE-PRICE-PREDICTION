from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # CORS ko globally enable karta hai

@app.route('/')
def home():
    return "🏠 Home Price Prediction API is running. Use /get_location_names or /predict_home_price"

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    if isinstance(locations, list):  # Ensure it's a list
        return jsonify({'locations': locations})
    else:
        return jsonify({'locations': []}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json() if request.is_json else request.form
    total_sqft = float(data.get('total_sqft', 0))
    location = data.get('location')
    bhk = int(data.get('bhk', 0))
    bath = int(data.get('bath', 0))

    estimated_price = util.get_estimated_price(location, total_sqft, bath, bhk)
    return jsonify({'estimated_price': estimated_price})

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
