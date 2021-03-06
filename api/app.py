from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'message': 'Hello from Liverpool Football API!'}), 200


if __name__ == "__main__":
    app.run(debug=True)