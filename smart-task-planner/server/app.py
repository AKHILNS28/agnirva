# server/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

# Simulated DB
TASKS_FILE = "tasks.json"

# OpenWeather API Key
API_KEY = "40f5f3a8eb7683389fbce7f33084bedd";

# Load tasks
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    task = request.get_json()
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify({"message": "Task added!"}), 201

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Bangalore")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = {
        "description": data["weather"][0]["description"],
        "temperature": data["main"]["temp"]
    }
    return jsonify(weather)

if __name__ == "__main__":
    app.run(debug=True)