from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class ListTicked(Resource):
    def get(self):
        path = "/ticket/list"
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, path, Status.cm_1)
        user_id = userdata.get("id")
        role = userdata.get("role")
        try:
            if role == 2:
                all_q = Ticket.query.all()
                output = []
                for i in all_q:
                    a = i.__dict__
                    a.pop('_sa_instance_state')
                    a.pop("date")
                    a.pop("isSloved")
                    a.pop("role")
                    a.pop("report_reason")
                    output.append(a)
                return output, 200
            else:
                return response(403, Status.c_403, path, "missing permission")
        except:
            return response(400, Status.c_400, path, Status.cm_2)