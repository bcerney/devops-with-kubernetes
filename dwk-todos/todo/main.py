import requests
from flask import Flask
from flask import current_app as app
from flask import jsonify, make_response, redirect, render_template, request, url_for

from .extensions import db
from .models import Task, TaskSchema


TASKS_SCHEMA = TaskSchema(many=True, exclude=("time_created",))


@app.route("/todos", methods=["GET", "POST"])
def todos():
    print(vars(request))
    if request.method == "POST" and request.is_json:
        req = request.get_json(force=True)

        task = Task(body=req.get("todo"))
        db.session.add(task)
        db.session.commit()

        tasks = Task.query.all()
        res = {"todos": TASKS_SCHEMA.dump(tasks)}
        print(res)

        return make_response(jsonify(res), 200)
    else:
        make_response(jsonify({"message": "Request body must be JSON"}), 400)

    tasks = Task.query.all()
    res = {"todos": TASKS_SCHEMA.dump(tasks)}
    return make_response(jsonify(res), 200)
