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
        try:
            if role == 2:
                all_q = Ticket.query.filter_by(support=True).all()
                output = []
                for i in all_q:
                    a = i.__dict__
                    a.pop('_sa_instance_state')
                    a.pop("date")
                    a.pop("isSloved")
                    a.pop("role")
                    a.pop("support")
                    a.pop("report_reason")
                    a.pop("task_id")
                    a.pop("response_title")
                    a.pop("response_body")
                    output.append(a)
                return output, 200
            else:
                return response(403, Status.c_403, request.path, "missing permission"), 403
        except:
            return response(400, Status.c_400, request.path, Status.cm_2), 400