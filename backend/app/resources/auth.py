from flask import jsonify
from .. import db
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

from ..models.user import User
from ..schemas.auth import AuthSchema
from ..helpers.jwt_esat import jwt_esat_refresh_token_required
from flask_smorest import Blueprint
from flask.views import MethodView

bp = Blueprint('Auth', 'auth', url_prefix='auth',
               description='auth stuff')


@bp.route('/login', methods=['POST'])
class Login(MethodView):
    @bp.arguments(AuthSchema)
    def post(self, login):
        username = login['username']
        password = login['password']
        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            ret = {
                'access_token': create_access_token(identity=username),
                'refresh_token': create_refresh_token(identity=username)
            }
            return jsonify(ret), 200
        else:
            return False


@bp.route('/refresh', methods=['POST'])
@jwt_esat_refresh_token_required
class Refresh(MethodView):
    def refresh():
        current_user = get_jwt_identity()
        ret = {
            'access_token': create_access_token(identity=current_user),
            'refresh_token': create_refresh_token(identity=current_user)
        }
        return jsonify(ret), 200


@bp.route('/logout', methods=['POST'])
class Logout(MethodView):
    def post():
        #logout_user()
        return True


@bp.route('/register', methods=['POST'])
class Register(MethodView):
    @bp.arguments(AuthSchema)
    def post(self, data):
        username = data['username']
        password = data['password']
        user = User(username=username,
                    password=password)
        db.session.add(user)
        db.session.commit()
        return 'ok', 200
