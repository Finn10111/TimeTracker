from .. import db
from datetime import datetime
from sqlalchemy import UniqueConstraint


class Task(db.Model):

    __table_args__ = (
        UniqueConstraint('name', 'user_id', name='unique_task_per_user'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now, nullable=True)
    timeperiods = db.relationship('Timeperiod', cascade='all, delete-orphan')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])

    def __repr__(self):
        return 'Task {}'.format(self.name)
