from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status

import jwt

class CreateTickte(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("task_id", type=str, help="task_id can not be blank")
        parser.add_argument("title", type=str, help="title can not be blank")
        parser.add_argument("body", type=str, help="body can not be blank")
        parser.add_argument("ticket_type", type=str, help="ticket_type can not be blank")
        parser.add_argument("ticket_id", type=str, help="ticket_id can not be blank")
        path = "/ticket"
        header = request.headers.get('Authorization')
        data = parser.parse_args()
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception as e:
            print(e)
            return response(401, Status.c_401, path, Status.cm_1)

        if userdata.get("status") == 3:  #? Status 3 == User Banned
            return response(200, Status.c_200, path)

        user_id = userdata.get("user_id")
        ticket = Ticket(task_id=data["task_id"], title=data["title"], body=data["body"], ticket_type=data["ticket_type"], ticket_id=data["ticket_id"], user_id=userdata["user_id"])
        ticket.save_to_db()
        
        return response(200, Status.c_200, path, "ticket successfully added")