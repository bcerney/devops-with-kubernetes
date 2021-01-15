from datetime import datetime

from .extensions import db, ma


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(500))

    def __repr__(self):
        return f"<Task {self.body}>"

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
