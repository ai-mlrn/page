# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows requests from your JS frontend

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hello from Python!"})

@app.route("/api/submit", methods=["POST"])
def receive_data():
    user_data = request.json
    return jsonify({"received": user_data}), 201

if __name__ == "__main__":
    app.run(port=5000, debug=True)
