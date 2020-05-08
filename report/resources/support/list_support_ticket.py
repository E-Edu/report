from flask_restful import Resource
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class ListSupportTicket(Resource):
    def get(self):
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        user_id = userdata.get("id")
        role = userdata.get("role")
        q = Ticket.query.filter_by(support=True, user_id=user_id).all()
        try:
            if q:
                return [x.return_report() for x in q], 200
            elif role == 2:
                return [x.return_report() for x in Ticket.query.filter_by(support=True).all()], 200
            else:
                return response(403, Status.c_403, request.path, "missing permission"), 403
        except:
            return response(400, Status.c_400, request.path, Status.cm_2), 400
