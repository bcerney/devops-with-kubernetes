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

# INDEX_IMG_PATH = "/app/files/index-img.jpeg"
# PICSUM_URL = "https://picsum.photos/300"


# def get_index_img():
#     if os.path.isfile(INDEX_IMG_PATH):
#         app.logger.info("Image exists")
#         img = Image.open(INDEX_IMG_PATH)
#         img.save("todo/static/index-img.jpeg")
#     else:
#         app.logger.info("Image not found, downloading now...")
#         response = requests.get(PICSUM_URL)
#         img = Image.open(BytesIO(response.content))
#         img.save(INDEX_IMG_PATH)
#         img.save("todo/static/index-img.jpeg")


# INDEX_IMG = get_index_img()


TODOS = ["todo1", "todo2"]


@app.route("/todos", methods=["GET", "POST"])
def todos():
    # TODO: figure out why is_json check not true
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
