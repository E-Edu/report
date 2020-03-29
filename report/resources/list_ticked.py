from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class ListTicked(Resource):
    def post(self):
        header = request.headers.get('Authorization')

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return {'error': 'INVALID_SESSION'}, 400

        user_id = userdata.get("id")
        role = userdata.get("role")

        if role == 2:
            all_q = Ticket.query.all()
            output = []
            for i in all_q:
                a = i.__dict__
                a.pop('_sa_instance_state')
                output.append(a)
            return {"output": output}
        else:
            return {}, 500