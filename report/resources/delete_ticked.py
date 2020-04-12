from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import Status, response

import jwt

class DeleteTicked(Resource):
    def delete(self, ticket_id):
        path = "/ticket/{ticket_id}"
        data = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(data, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, path, Status.cm_1)

        if ticket_id is None and ticket_id > 0:
            return request(400, Status.c_400, path)
        try:
            ticket = Ticket.query.get_or_404(ticket_id)
            ticket.delete_from_db()
        except Exception:
            return request(400, Status.c_400, path, "invalid ticket_id")

        return response(200, Status.c_200, path, "ticket successfully deleted")