from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status

import jwt

class CreateTickte(Resource):
    def post(self):
        path = "/ticket"
        data = request.json
        header = request.headers.get('Authorization')

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception as e:
            print(e)
            return response(401, Status.c_401, path, Status.cm_1)

        if data is None:
            return response(400,  Status.c_400, path, Status.cm_2)

        if userdata.get("status") == 4:  #? Status 4 == User Banned
            return response(200, Status.c_200, path)

        user_id = userdata.get("user_id")
        ticket = Ticket(taskId=data['task_id'], title=data['title'], body=data['body'], user_id=user_id)
        ticket.save_to_db()
        
        return response(200, Status.c_200, path, "ticket successfully added")