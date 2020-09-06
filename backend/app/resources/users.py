from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.user import UserSchema, UserQuerySchema
from ..models.user import User
from sqlalchemy import func

bp = Blueprint('User', 'users', url_prefix='users',
               description='Operations on users')


@bp.route('/')
class Users(MethodView):

    @bp.arguments(UserQuerySchema, location="query")
    @bp.response(UserSchema(many=True))
    def get(self, args):
        users = User.query.order_by(User.id).all()
        return users
