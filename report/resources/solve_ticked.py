from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class SolveTicked(Resource):
    def put(self, ticked_id):
        data = request.json
        header = request.headers.get('Authorization')

        if header is not None and 'is_troll' in data:
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
                # TODO: bann user
                # User Microservice not Ready
                return {}, 501
            else:
                ticked_q = Ticket.query.get_or_404(ticked_id)
                if ticked_q is not None:
                    ticked_q.isSloved = True
                db.session.commit()
                return {}, 200
        else:
            return {'forbidden': 'INVALID_PERMISSION'}, 403