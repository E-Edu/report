from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.models.ticket import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class EditSupportTicket(Resource):
    def put(self, ticket_id):
        parser = reqparse.RequestParser()
        parser.add_argument("title", type=str, help="title can not be blank")
        parser.add_argument("body", type=str, help="body can not be blank")
        data = parser.parse_args()
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except:
            return response(401, Status.c_401, request.path, Status.cm_1), 401
        user_id = userdata.get('id')
        role = userdata.get('role')
        if data["title"] == None or data["body"] == None:
            return response(400, Status.c_400, request.path, Status.cm_2), 400
        try:
            try:
                ticked_q = Ticket.query.get_or_404(ticket_id)
            except:
                return response(400, Status.c_400, request.path, "invalid ticket_id"), 400
            if role == 2:
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                db.session.commit()
                return response(200, Status.c_200, request.path, "ticket successfully edit"), 200
            if user_id != ticked_q.user_id:
                return response(403, Status.c_403, request.path, "wrong identity or missing permission"), 403
            if user_id:
                ticked_q.title = data['title']
                ticked_q.body = data['body']
                db.session.commit()
                return response(200, Status.c_200, request.path, "ticket successfully edit"), 200
            else:
                return response(400, Status.c_400, request.path), 400
        except:
            return response(400, Status.c_400, request.path, Status.cm_2), 400