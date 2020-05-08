from flask_restful import Resource
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class ListTicket(Resource):
    def get(self):
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        user_id = userdata.get("id")
        role = userdata.get("role")
        try:
            if role == 2:
                all_q = Ticket.query.filter_by(support=False).all()
                return [x.return_report() for x in Ticket.query.all()], 200
            else:
                return response(403, Status.c_403, request.path, "missing permission"), 403
        except:
            return response(400, Status.c_400, request.path, Status.cm_2), 400
