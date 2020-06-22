from flask_jwt_extended import JWTManager, jwt_required
from app.models.user import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user is not None and user.verify_password(password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()

