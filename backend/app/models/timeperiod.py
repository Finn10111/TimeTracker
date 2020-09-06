from .. import db


class Timeperiod(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    task = db.relationship("Task", foreign_keys=[task_id])
    start = db.Column(db.DateTime(timezone=True), nullable=False)
    end = db.Column(db.DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return 'Timeperiod task_id: {}, start: {}, end: {}'.format(self.task_id, self.start, self.end)
