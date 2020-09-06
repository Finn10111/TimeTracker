from .. import db
from datetime import datetime


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now, nullable=True)
    timeperiods = db.relationship('Timeperiod', cascade='all, delete-orphan')

    def __repr__(self):
        return 'Task {}'.format(self.name)
