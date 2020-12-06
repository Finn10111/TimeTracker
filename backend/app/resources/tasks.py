from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.task import TaskSchema, TaskQuerySchema
from ..models.task import Task
from ..helpers.userHelper import UserHelper
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('Task', 'tasks', url_prefix='tasks',
               description='Operations on tasks')


@bp.route('/')
class Tasks(MethodView):

    @bp.arguments(TaskQuerySchema, location="query")
    @bp.response(TaskSchema(many=True))
    @jwt_required
    def get(self, args):
        user_id = UserHelper.get_id_by_identity(get_jwt_identity())
        tasks = Task.query.filter_by(user_id=user_id).order_by(Task.name).all()
        return tasks

    @bp.arguments(TaskSchema)
    @bp.response(TaskSchema, code=201)
    @jwt_required
    def post(self, new_task):
        new_task.user_id = UserHelper.get_id_by_identity(get_jwt_identity())
        db.session.add(new_task)
        db.session.commit()
        return new_task


@bp.route('/<task_id>')
class TaskById(MethodView):
    @bp.response(code=204)
    @jwt_required
    def delete(self, task_id):
        user_id = UserHelper.get_id_by_identity(get_jwt_identity())
        task = Task.query.filter_by(id=task_id, user_id=user_id).first()
        db.session.delete(task)
        db.session.commit()
