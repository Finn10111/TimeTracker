from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.timeperiod import TimeperiodSchema, TimeperiodQuerySchema
from ..models.timeperiod import Timeperiod

bp = Blueprint('Timeperiod', 'timeperiods', url_prefix='timeperiods',
               description='Operations on timeperiods')


@bp.route('/')
class Timeperiods(MethodView):

    @bp.arguments(TimeperiodQuerySchema, location="query")
    @bp.response(TimeperiodSchema(many=True))
    def get(self, args):
        timeperiods = Timeperiod.query.all()
        return timeperiods


    @bp.arguments(TimeperiodSchema)
    @bp.response(TimeperiodSchema, code=201)
    def post(self, new_timeperiod):
        print(new_timeperiod)
        db.session.add(new_timeperiod)
        db.session.commit()
        return new_timeperiod


@bp.route('/<timeperiod_id>/')
class TimeperiodById(MethodView):
    @bp.arguments(TimeperiodSchema)
    @bp.response(TimeperiodSchema)
    def put(self, update_timeperiod, timeperiod_id):
        timeperiod = Timeperiod.query.get(timeperiod_id)

        timeperiod.end = update_timeperiod.end

        db.session.add(timeperiod)
        db.session.commit()

        return update_timeperiod
