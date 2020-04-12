from flask_restful import Resource
from flask import request
from report import db
from report.database import Ticket
from report.config import VenVar

import jwt

class DeleteTicked(Resource):
    def delete(self, ticket_id):
        data = request.headers.get('Authorization')
        try:
            userdata = jwt.decode(data, VenVar.JWT_SEC, VenVar.JWT_ALGORITHMS)
        except Exception:
            return {'error': 'INVALID_SESSION'}, 400

        if ticket_id is None and ticket_id > 0:
            return {'error': 'MISSING_DATA'}, 400
        try:
            ticket = Ticket.query.get_or_404(ticket_id)
            ticket.delete_from_db()
        except Exception:
            return {'error': 'DATABASE_ERROR'}, 500

        return {}, 200