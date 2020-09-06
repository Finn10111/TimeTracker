from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.task import TaskSchema, TaskQuerySchema
from ..models.task import Task
from flask_jwt_extended import jwt_required

bp = Blueprint('Task', 'tasks', url_prefix='tasks',
               description='Operations on tasks')


@bp.route('/')
class Tasks(MethodView):

    @bp.arguments(TaskQuerySchema, location="query")
    @bp.response(TaskSchema(many=True))
    @jwt_required
    def get(self, args):
        tasks = Task.query.order_by(Task.name).all()
        return tasks

    @bp.arguments(TaskSchema)
    @bp.response(TaskSchema, code=201)
    @jwt_required
    def post(self, new_task):
        db.session.add(new_task)
        db.session.commit()
        return new_task


@bp.route('/<task_id>')
class TaskById(MethodView):
    @bp.response(code=204)
    @jwt_required
    def delete(self, task_id):
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
