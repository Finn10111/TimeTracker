from .. import ma
from ..models.timeperiod import Timeperiod
from marshmallow import fields
from .namespacedSchema import NamespacedSchema


class TimeperiodQuerySchema(ma.Schema):
    class Meta:
        strict = True

    query = fields.String()


class TimeperiodSchema(NamespacedSchema):

    class Meta:
        strict = True
        model = Timeperiod
        name = "timeperiod"
        plural_name = "timeperiods"
