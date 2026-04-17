#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# yaddaşda saxlanılan data
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


# 1. root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# 2. status endpoint
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# 3. bütün usernames
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))


# 4. specific user
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# 5. add user (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        username = data.get("username")

        if not username:
            return jsonify({"error": "Username is required"}), 400

        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        users[username] = data

        return jsonify({
            "message": "User added",
            "user": data
        }), 201

    except:
        return jsonify({"error": "Invalid JSON"}), 400


# server run
if __name__ == "__main__":
    app.run()
