from todo import create_app
from todo.extensions import db
from todo.models import Task

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Task": Task}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
