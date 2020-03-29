from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class EditTicked(Resource):
    def put(self, ticket_id):
        data = request.json
        header = request.headers.get('Authorization')

        if data is not None and all(key in data for key in ('title', 'body')):
            pass
        else:
            return {'error': 'Missing Keys'}, 400

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return {'error': 'Invalid Session'}, 400

        user_id = userdata.get('id')
        role = userdata.get('role')

        if role == 2:
            ticked_q = Ticket.query.get_or_404(ticket_id)
            if ticked_q is not None:
                ticked_q.taskId = data['task_id']
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                ticked_q.user_id = user_id
                ticked_q.role = role

                db.session.commit()
                return {}, 200
            else:
                return {}, 500

        if role == 1 or role == 0:
            ticked_q = Ticket.query.get_or_404(ticket_id)

            if user_id != ticked_q.user_id:
                return {'forbidden': 'wrong user id'}, 403

            if ticked_q is not None:
                ticked_q.taskId = data['task_Id']
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                ticked_q.user_id = user_id
                ticked_q.role = role

                db.session.commit()
                return {}, 200
            else:
                return {}, 500