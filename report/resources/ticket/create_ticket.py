from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class CreateTicket(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("task_id", type=str, help="task_id can not be blank")
        parser.add_argument("title", type=str, help="title can not be blank")
        parser.add_argument("body", type=str, help="body can not be blank")
        parser.add_argument("report_reason", type=str, help="report_reason can not be blank")
        header = request.headers.get('Authorization')
        data = parser.parse_args()
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        if userdata.get("status") == 3:  #? Status 3 == User Banned
            return response(200, Status.c_200, request.path), 200
        ticket = Ticket(task_id=data["task_id"], title=data["title"], body=data["body"], user_id=str(userdata["id"]), role=userdata["role"], report_reason=data["report_reason"])
        ticket.save_to_db()
        return response(201, Status.c_201, request.path, "report ticket successfully added"), 201