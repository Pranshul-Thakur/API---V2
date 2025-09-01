from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Task Manager API works"

@app.route("/tasks", methods =["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>", methods = ["GET"])
def get_single_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error" : "Id not present"}), 404

@app.route("/tasks", methods = ["POST"])
def create_tasks():
    data = request.json
    task = {
        "id" : len(tasks) + 1,
        "title" : data["title"],
        "description" : data.get("description", ""),
        "status" : "pending"
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods = ["PUT", "PATCH"])
def update_tasks(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "task not found"}), 404
    
    data = request.json
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["status"] = data.get("status", task["status"])
    return jsonify(task)

@app.route("/tasks/<int:task_id>", methods = ["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message" : "Task deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)