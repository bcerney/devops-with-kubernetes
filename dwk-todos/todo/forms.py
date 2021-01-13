from flask_wtf import FlaskForm
from wtforms import (
    HiddenField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.widgets import CheckboxInput, ListWidget


class AddTodoForm(FlaskForm):
    todo = StringField("TODO", validators=[DataRequired()])
    add_todo_submit = SubmitField("Add TODO")

    def __repr__(self):
        return f"<AddTodoForm: todo={self.todo}>"
