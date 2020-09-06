from .. import ma
from ..models.user import User
from marshmallow import fields
from .namespacedSchema import NamespacedSchema


class UserQuerySchema(ma.Schema):
    class Meta:
        strict = True
  
    query = fields.String()


class UserSchema(NamespacedSchema):

    class Meta:
        strict = True
        model = User
        name = "user"
        plural_name = "users"
