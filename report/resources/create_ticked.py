from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class CreateTickte(Resource):
    data = request.json
    header = request.headers.get('Authorization')

    def post(self):
        if data is None:
            return {'error': 'Missing Keys'}, 400

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception as e:
            print(e)
            return {'error': 'INVALID_SESSION'}, 400

        if userdata.get("status") == 4:  # Status 4 == User Banned
            return {}, 200

        user_id = userdata.get("id")
        ticket = Ticket(taskId=data['task_id'], title=data['title'], body=data['body'], TicketType=data['TicketType'], user_id=user_id)
        db.session.add(ticket)
        db.session.commit()
        
        return {}, 200