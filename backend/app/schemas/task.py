from .. import ma
from ..models.task import Task
from ..schemas.timeperiod import TimeperiodSchema
from marshmallow import fields
from .namespacedSchema import NamespacedSchema


def get_timeperiods_schema():
    timeperiodSchema = TimeperiodSchema()
    timeperiodSchema.context['noenvelope'] = True
    return timeperiodSchema


class TaskQuerySchema(ma.Schema):
    class Meta:
        strict = True

    query = fields.String()


class TaskSchema(NamespacedSchema):

    class Meta:
        strict = True
        model = Task
        name = "task"
        plural_name = "tasks"

    timeperiods = ma.Nested(get_timeperiods_schema, many=True, exlude=('task',))
