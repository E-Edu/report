from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class SolveTicket(Resource):
    def put(self, ticket_id):
        parser = reqparse.RequestParser()
        parser.add_argument("response_title", type=bool, help="response_title can not be blank")
        parser.add_argument("response_body", type=bool, help="response_body can not be blank")
        data = parser.parse_args()
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        if not data["response_title"] or not data["response_body"]:
            return response(400,  Status.c_400, request.path, Status.cm_2), 400
        role = userdata.get('role')
        try:
            ticket_q = Ticket.query.get_or_404(ticket_id)
        except:
            return response(400, Status.c_400, request.path, "invalid ticket_id"), 400
        if role == 2 and ticket_q:
            ticket_q.response_title = data["response_title"]
            ticket_q.response_body = data["response_body"]
            db.session.commit()
            return response(200, Status.c_200, request.path), 200
        else:
            return response(403, Status.c_403, request.path, "permission denied"), 403