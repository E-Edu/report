from flask_restful import Resource
from flask import request
from report.models.ticket import Ticket
from report.resources.ticket.parser import CreateTicketParser
from report.require.require_jwt import require_jwt
from report.response import response, Status

class CreateTicket(Resource):
    def post(self):
        data = CreateTicketParser.parser_args()
        header = request.headers.get('Authorization')
        jwt = require_jwt(header)
        if jwt:
            if jwt.get("status") == 3:  #? Status 3 == User Banned
                return response(200, Status.c_200, request.path), 200
            ticket = Ticket(task_id=data["task_id"], title=data["title"], body=data["body"], user_id=str(jwt["id"]), role=jwt["role"], report_reason=data["report_reason"])
            ticket.save_to_db()
            return response(201, Status.c_201, request.path, "report ticket successfully added"), 201
        else:
            return response(401, Status.c_401, request.path, Status.cm_1), 401