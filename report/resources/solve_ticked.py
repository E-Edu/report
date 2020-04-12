from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status

import jwt

class SolveTicked(Resource):
    def put(self, ticket_id):
        path = "/ticket/{ticket_id}/answer"
        data = request.json
        header = request.headers.get('Authorization')

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, path, Status.cm_1)

        if header and 'is_troll' in data:
            pass
        else:
            return response(400,  Status.c_400, path, Status.cm_2)

        role = userdata.get('role')
        ticket_q = Ticket.query.get_or_404(ticket_id)
        if role == 2 and ticket_q:
            if ticket_q.isSloved:
                return response(200, Status.c_200, path, "ticket already markt as troll")
            else:
                ticket_q.isSloved = True
                db.session.commit()
                return response(200, Status.c_200, path, "ticket markt as troll")
        else:
            return response(403, Status.c_403, path, "permission denied")