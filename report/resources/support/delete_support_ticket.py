from flask_restful import Resource
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import Status, response
import jwt

class DeleteSupportTicket(Resource):
    def delete(self, ticket_id):
        data = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(data, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        try:
            ticket = Ticket.query.get_or_404(ticket_id)
        except:
            return response(400, Status.c_400, request.path, "invalid ticket_id"), 400
        if ticket:
            try:
                if ticket.user_id == userdata["id"] or userdata["role"] == 2:
                    ticket.delete_from_db()
                    return response(200, Status.c_200, request.path, "ticket successfully deleted"), 200
            except:
                return response(400, Status.c_400, request.path, Status.cm_2), 400
        else:
            return response(400, Status.c_400, request.path), 400