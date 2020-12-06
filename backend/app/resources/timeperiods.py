from .. import db
from flask.views import MethodView
from flask_smorest import Blueprint
from ..schemas.timeperiod import TimeperiodSchema, TimeperiodQuerySchema
from ..models.timeperiod import Timeperiod
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..helpers.userHelper import UserHelper

bp = Blueprint('Timeperiod', 'timeperiods', url_prefix='timeperiods',
               description='Operations on timeperiods')


@bp.route('/')
class Timeperiods(MethodView):
    @bp.arguments(TimeperiodSchema)
    @bp.response(TimeperiodSchema, code=201)
    @jwt_required
    def post(self, new_timeperiod):
        # check if given task belongs to user
        if UserHelper.timepreiod_belong_to_user(new_timeperiod):
            db.session.add(new_timeperiod)
            db.session.commit()
            return new_timeperiod
        else:
            return {'error': 'this is not your task'}, 403


@bp.route('/<timeperiod_id>/')
class TimeperiodById(MethodView):
    @bp.arguments(TimeperiodSchema)
    @bp.response(TimeperiodSchema)
    @jwt_required
    def put(self, update_timeperiod, timeperiod_id):
        # check if timeperiod belongs to user
        timeperiod = Timeperiod.query.get(timeperiod_id)
        if UserHelper.timepreiod_belong_to_user(timeperiod):
            timeperiod.end = update_timeperiod.end
            db.session.add(timeperiod)
            db.session.commit()
            return update_timeperiod
        else:
            return {'error': 'this is not your task'}, 403

    @bp.response(code=204)
    @jwt_required
    def delete(self, timeperiod_id):
        # check if timeperiod belongs to user
        timeperiod = Timeperiod.query.get(timeperiod_id)
        if UserHelper.timepreiod_belong_to_user(timeperiod):
            db.session.delete(timeperiod)
            db.session.commit()
        else:
            return {'error': 'this is not your task'}, 403
