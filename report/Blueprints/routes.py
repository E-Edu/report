import json
import os

import jwt
from flask import Blueprint, request, jsonify

from report import db
from report.database import Ticket

main_page = Blueprint('main-routes', __name__)


@main_page.route('/ticket', methods=['POST'])
def ticked_create():
    data = request.json
    header = request.headers.get('Authorization')

    if data is None:
        return jsonify({'error': 'Missing Keys'}), 400

    try:
        userdata = jwt.decode(header, os.environ.get('JWT_SECRET'), algorithms=['HS256'])
    except Exception as e:
        print(e)
        return jsonify({'error': 'INVALID_SESSION'}), 400

    if userdata.get("status") == 4: # Status 4 == User Banned
        return jsonify({}), 200

    user_id = userdata.get("id")
    ticket = Ticket(taskId=data['task_id'], title=data['title'],
                    body=data['body'], TicketType=data['TicketType'], user_id=user_id)
    db.session.add(ticket)
    db.session.commit()
    return jsonify({}), 200


@main_page.route('/ticket/delete/<id>', methods=['DELETE'])
def ticked_delete(id):
    data = request.headers.get('Authorization')
    try:
        userdata = jwt.decode(data, os.environ.get(
            'JWT_SECRET'), algorithms=['HS256'])
    except Exception:

        return jsonify({'error': 'INVALID_SESSION'}), 400

    if id is None and id > 0:
        return jsonify({'error': 'MISSING_DATA'}), 400
    try:
        ticket = Ticket.query.get_or_404(id)
        db.session.delete(ticket)
        db.session.commit()
    except Exception:
        return jsonify({'error': 'DATABASE_ERROR'}), 500

    return jsonify({}), 200


@main_page.route('/ticket/list', methods=['POST'])
def ticked_list():
    header = request.headers.get('Authorization')

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['HS256'])
    except Exception:
        return jsonify({'error': 'INVALID_SESSION'}), 400

    user_id = userdata.get("id")
    role = userdata.get("role")

    if role == 2:
        all_q = Ticket.query.all()
        output = []
        for i in all_q:
            a = i.__dict__
            a.pop('_sa_instance_state')
            output.append(a)
        return jsonify(output)
    else:
        return jsonify({}), 500


@main_page.route('/ticket/<id>/edit', methods=['PUT'])
def ticked_edit(id):
    data = request.json
    header = request.headers.get('Authorization')

    if data is not None and all(key in data for key in ('title', 'body')):
        pass
    else:
        return jsonify({'error': 'Missing Keys'}), 510

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['HS256'])
    except Exception:
        return jsonify({'error': 'Invalid Session'}), 510

    user_id = userdata.get('id')
    role = userdata.get('role')
    print(id)
    if role == 2:
        ticked_q = Ticket.query.get_or_404(id)
        if ticked_q is not None:
            ticked_q.taskId = data['task_id']
            ticked_q.title = data['title']
            ticked_q.body = data['body']
            ticked_q.user_id = user_id
            ticked_q.role = role

            db.session.commit()
            return jsonify({}), 200
        else:
            return jsonify({}), 500

    if role == 1 or role == 0:
        ticked_q = Ticket.query.get_or_404(id)

        if user_id != ticked_q.user_id:
            return jsonify({'forbidden': 'wrong user id'}), 403

        if ticked_q is not None:
            ticked_q.taskId = data['task_Id']
            ticked_q.title = data['title']
            ticked_q.body = data['body']
            ticked_q.user_id = user_id
            ticked_q.role = role

            db.session.commit()
            return jsonify({}), 200
        else:
            return jsonify({}), 500


@main_page.route('/ticket/<id>/answer', methods=['PUT'])
def ticked_slove(id):
    data = request.json
    header = request.headers.get('Authorization')

    if header is not None and 'is_troll' in data:
        pass
    else:
        return jsonify({'error': 'Missing Keys'}), 510

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['HS256'])
    except Exception:
        return jsonify({'error': 'Invalid Session'}), 510

    role = userdata.get('role')
    if role == 2:
        if data['is_troll']:
            # TODO: bann user
            # User Microservice not Ready
            print("User Banned")
            return jsonify({}), 500
        else:
            ticked_q = Ticket.query.get_or_404(id)
            if ticked_q is not None:
                ticked_q.isSloved = True
            db.session.commit()
            return jsonify({}), 500
    else:
        jsonify({'forbidden': 'INVALID_PERMISSION'}), 403
