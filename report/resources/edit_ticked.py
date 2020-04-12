from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status

import jwt

class EditTicked(Resource):
    def put(self, ticket_id):
        path = "/ticket/{ticket_id}/edit"
        data = request.json
        header = request.headers.get('Authorization')

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return response(401, Status.c_401, path, Status.cm_1)

        if data and all(key in data for key in ('title', 'body')):
            pass
        else:
             return response(400,  Status.c_400, path, Status.cm_2)

        user_id = userdata.get('user_id')
        role = userdata.get('role')

        if role == 2:
            ticked_q = Ticket.query.get_or_404(ticket_id)
            if ticked_q:
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                db.session.commit()
                return response(200, Status.c_200, path, "ticket successfully edit")

        elif role == 1 or role == 0 or role == 3:
            ticked_q = Ticket.query.get_or_404(ticket_id)

            if user_id != ticked_q.user_id:
                return response(403, Status.c_403, path, "wrong identity or missing permission")

            if ticked_q:
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                db.session.commit()
                return response(200, Status.c_200, path, "ticket successfully edit")
            else:
                return response(400, Status.c_400, path, Status.cm_2)