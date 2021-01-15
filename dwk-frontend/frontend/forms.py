from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired


class AddTodoForm(FlaskForm):
    todo = StringField("TODO", validators=[DataRequired()])
    add_todo_submit = SubmitField("Add TODO")

    def __repr__(self):
        return f"<AddTodoForm: todo={self.todo}>"
