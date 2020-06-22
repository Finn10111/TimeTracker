from marshmallow import fields
from .. import ma


class AuthSchema(ma.Schema):
    username = fields.String()
    password = fields.String()

