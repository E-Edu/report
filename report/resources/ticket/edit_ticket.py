from flask_restful import Resource
from flask import request
from report import db
from report.models.ticket import Ticket
from report.response import response, Status
from report.resources.ticket.parser import EditTicketParser
from report.require.require_jwt import require_jwt

class EditTicket(Resource):
    def put(self, ticket_id):
        header = request.headers.get('Authorization')
        data = EditTicketParser.parser_args()
        jwt = require_jwt(header)
        if jwt:
            try:
                try:
                    ticket_q = Ticket.query.get_or_404(ticket_id)
                except:
                    return response(400, Status.c_400, request.path, "invalid ticket_id"), 400
                if ticket_q.user_id == jwt["id"] or jwt["role"] == 2:
                    ticket_q.title = data['title']
                    ticket_q.body = data['body']
                    db.session.commit()
                    return response(200, Status.c_200, request.path, "ticket successfully edit"), 200
            except:
                return response(400, Status.c_400, request.path, Status.cm_2), 400
        else:
            return response(401, Status.c_401, request.path, Status.cm_1), 401