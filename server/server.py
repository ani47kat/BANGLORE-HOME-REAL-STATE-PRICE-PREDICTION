from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import util
import os

# Create Flask app; static_folder is the folder of your frontend files
app = Flask(
    __name__,
    static_folder="../client",     # relative path from server/ to client/
    static_url_path=""             # serve static files at root (so "/" works)
)
CORS(app)

@app.route('/')
def serve_index():
    # This will return client/index.html
    return app.send_static_file("index.html")

# You can also serve other frontend routes if needed, like /about etc:
# @app.route('/somepage')
# def serve_page():
#     return app.send_static_file("somepage.html")

@app.route('/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    if isinstance(locations, list):
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
    port = int(os.environ.get("PORT", 5000))
    # Do *not* use debug=True in production; in development it's okay
    app.run(host="0.0.0.0", port=port)
