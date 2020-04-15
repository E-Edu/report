from flask_restful import Resource, reqparse
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar
from report.response import response, Status
import jwt

class SolveTicked(Resource):
    def put(self, ticket_id):
        parser = reqparse.RequestParser()
        parser.add_argument("is_troll", type=bool, help="is_troll can not be blank")
        path = "/ticket/{ticket_id}/answer"
        data = parser.parse_args()
        header = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except:
            return response(401, Status.c_401, path, Status.cm_1)
        if not data["is_troll"] or data["is_troll"] != True:
            return response(400,  Status.c_400, path, Status.cm_2)
        role = userdata.get('role')
        try:
            ticket_q = Ticket.query.get_or_404(ticket_id)
        except:
            return response(400, Status.c_400, path, "invalid ticket_id")
        if role == 2 and ticket_q:
            if ticket_q.isSloved:
                return response(200, Status.c_200, path, "ticket already markt as troll")
            else:
                ticket_q.isSloved = True
                db.session.commit()
                return response(200, Status.c_200, path, "ticket markt as troll")
        else:
            return response(403, Status.c_403, path, "permission denied")