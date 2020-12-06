from ..models.user import User
from flask_jwt_extended import get_jwt_identity


class UserHelper:
    def get_id_by_identity(self):
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        return user.id
