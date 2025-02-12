from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []  # Global list to store tasks


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {"id": len(tasks) + 1, "title": data["title"], "done": False}
    tasks.append(task)
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = request.json.get("done", task["done"])
            return jsonify(task)
    return jsonify({"error": "Task not found"})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return "", 204
    return jsonify({"error": "Task not found"})


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/clear", methods=["DELETE"])
def clear_tasks():
    tasks.clear()
    return jsonify({"message": "All tasks cleared"}), 200


if __name__ == "__main__":
    app.run(debug=True)
