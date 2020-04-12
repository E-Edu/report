from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class SolveTicked(Resource):
    def put(self, ticket_id):
        data = request.json
        header = request.headers.get('Authorization')

        if header and 'is_troll' in data:
            pass
        else:
            return {'error': 'Missing Keys'}, 400

        try:
            userdata = jwt.decode(header, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return {'error': 'Invalid Session'}, 400

        role = userdata.get('role')
        if role == 2:
            if data['is_troll']:
                return {"msg": "ticket already markt as troll"}, 200
            else:
                ticked_q = Ticket.query.get_or_404(ticket_id)
                if ticked_q is not None:
                    ticked_q.isSloved = True
                db.session.commit()
                return {"msg": "ticket markt as troll"}, 201
        else:
            return {'error': 'INVALID PERMISSION'}, 403