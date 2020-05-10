from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.models.ticket import Ticket
from report.response import response, Status
from report.require.require_jwt import require_jwt
from report.resources.ticket.parser import SolveTicketParser

class SolveTicket(Resource):
    def put(self, ticket_id):
        header = request.headers.get('Authorization')
        data = SolveTicketParser.parser_args()
        jwt = require_jwt(header)
        if jwt:
            if not data["is_troll"]:
                return response(400,  Status.c_400, request.path, Status.cm_2), 400
            try:
                ticket_q = Ticket.query.get_or_404(ticket_id)
            except:
                return response(400, Status.c_400, request.path, "invalid ticket_id"), 400
            if jwt["role"] == 2 and ticket_q:
                if ticket_q.isSloved:
                    return response(200, Status.c_200, request.path, "ticket already markt as troll"), 200
                else:
                    ticket_q.isSloved = True
                    db.session.commit()
                    return response(200, Status.c_200, request.path, "ticket markt as troll"), 200
            else:
                return response(403, Status.c_403, request.path, "permission denied"), 403
        else:
            return response(401, Status.c_401, request.path, Status.cm_1), 401