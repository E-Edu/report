from flask_restful import Resource
from flask import request
from report import db
from report.models.ticket import Ticket
from report.require.require_jwt import require_jwt
from report.response import Status, response

class DeleteTicket(Resource):
    def delete(self, ticket_id):
        data = request.headers.get('Authorization')
        jwt = require_jwt(data)
        if jwt:
            ticket = Ticket.query.get_or_404(ticket_id)
            print(ticket)
            if ticket:
                try:
                    if ticket.user_id == jwt["id"] or jwt["role"] == 2:
                        ticket.delete_from_db()
                        return response(200, Status.c_200, request.path, "ticket successfully deleted"), 200
                    else:
                        return response(401, Status.c_401, request.path, Status.cm_1), 401
                except:
                    return response(400, Status.c_400, request.path, Status.cm_2), 400
            else:
                return response(400, Status.c_400, request.path), 400
        else:
            return response(401, Status.c_401, request.path, Status.cm_1), 401