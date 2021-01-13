import logging
import os
import uuid
from io import BytesIO

import requests
from flask import Flask
from flask import current_app as app
from flask import make_response, jsonify, redirect, render_template, request, url_for
from PIL import Image

from .forms import AddTodoForm



TODOS = ["todo1", "todo2"]


@app.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method == "POST" and request.is_json:
        req = request.get_json(force=True)
        todo = req.get("todo")
        TODOS.append(todo)

        # print() works for stdout k8s logs, use it
        print(TODOS)

        res = {"todos": TODOS}
        return make_response(jsonify(res), 200)
    else:
        make_response(jsonify({"message": "Request body must be JSON"}), 400)
    return make_response(jsonify({"todos": TODOS}), 200)
