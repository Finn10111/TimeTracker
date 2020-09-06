from marshmallow import fields
from .. import ma


class AuthSchema(ma.Schema):
    identification = fields.String()
    password = fields.String()

