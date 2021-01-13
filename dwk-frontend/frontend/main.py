import logging
import os
import uuid
from io import BytesIO

import requests
from flask import Flask
from flask import current_app as app
from flask import redirect, render_template, request, url_for
from PIL import Image

from .forms import AddTodoForm

# INDEX_IMG_PATH = "/app/files/index-img.jpeg"
INDEX_IMG_PATH = "frontend/static/index-img.jpeg"
PICSUM_URL = "https://picsum.photos/300"
DWK_TODOS_SVC_URL = "http://dwk-todos-svc/todos"

# Content type must be included in the header
TODOS_POST_HEADERS = {"mimetype": "application/json"}


def get_index_img():
    if os.path.isfile(INDEX_IMG_PATH):
        app.logger.info("Image exists")
        # img = Image.open(INDEX_IMG_PATH)
        # img.save("todo/static/index-img.jpeg")
    else:
        app.logger.info("Image not found, downloading now...")
        response = requests.get(PICSUM_URL)
        img = Image.open(BytesIO(response.content))
        img.save(INDEX_IMG_PATH)
        # img.save("todo/static/index-img.jpeg")


get_index_img()


@app.route("/", methods=["GET", "POST"])
def index():
    add_todo_form = AddTodoForm(request.form)

    if request.method == "POST" and add_todo_form.validate_on_submit():
        todo = {"todo": add_todo_form.todo.data}

        todos_res = requests.post(
            DWK_TODOS_SVC_URL, json=todo)
        app.logger.debug(f"todos_res: {todos_res}")
        todos = todos_res.json().get("todos")

        add_todo_form = AddTodoForm()
        return render_template(
            "index.html", todos=todos, todos_res=todos_res, add_todo_form=add_todo_form
        )

    # Get all todos
    todos_res = requests.get(DWK_TODOS_SVC_URL).json()
    todos = todos_res.get("todos")

    return render_template("index.html", todos=todos, add_todo_form=add_todo_form)