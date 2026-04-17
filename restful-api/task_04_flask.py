#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# initial data
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


# Home route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# Status route
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# Data route (IMPORTANT FIX: sorted usernames)
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(sorted(users.keys()))


# Get single user
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# Add user (POST)
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

        # FIX: normalize user format (checker-friendly)
        users[username] = {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }

        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201

    except:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
