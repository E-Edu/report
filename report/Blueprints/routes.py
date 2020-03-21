from flask import Blueprint, request, jsonify, redirect
from report.database import Ticket
from report import db
import jwt
import os
import json

main_page = Blueprint('main-routes', __name__)


@main_page.route('/ticket/create', methods=['POST'])
def ticked_create():
    data = request.json
    header = request.headers.get('Authorization')
    
    if data is None or header is None or any(key in data for key in ('session', 'task_id', 'title', 'body', 'TicketType')) is False:
        return jsonify({'error': 'Missing Keys'}), 400

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['ES256'])
    except Exception:
        return jsonify({'error': 'INVALID_SESSION'}), 400

    user_id = userdata.get("id")

    ticket = Ticket(taskid=data['task_id'], title=data['title'],
                    body=data['body'], TicketType=data['TicketType'], user_id=user_id)
    db.session.add(ticket)
    db.session.commit()
    return jsonify({}), 200


@main_page.route('/ticket/delete/<id>', methods=['DELETE'])
def ticked_delete(id):
    data = request.headers.get('Authorization')
    try:
        userdata = jwt.decode(data['session'], os.environ.get(
            'JWT_SECRET'), algorithms=['ES256'])
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


@main_page.route('/ticket/list')
def ticked_list():
    header = request.headers.get('Authorization')

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['ES256'])
    except Exception:
        return jsonify({'error': 'INVALID_SESSION'}), 400

    user_id = userdata.get("id")
    role = userdata.get("role")

    if role == 2:
        all_q = Ticket.query.all()
        output = json.dump(all_q)
        return jsonify(output)
    else:
        return jsonify({}), 500


@main_page.route('/ticket/edit/<id>', methods=['PUT'])
def ticked_edit(id):

    data = request.json
    header = request.headers.get('Authorization')

    if data is not None and all(key in data for key in ('session', 'task_id', 'title', 'body', 'TicketType')):  # ! save session
        print("Works")
    else:
        return jsonify({'error': 'Missing Keys'}), 510

    try:
        userdata = jwt.decode(header, os.environ.get(
            'JWT_SECRET'), algorithms=['ES256'])
    except Exception:
        return jsonify({'error': 'Invalid Session'}), 510

    user_id = userdata.get('id')
    role = userdata.get('role')

    if role == 2:
        ticked_q = Ticket.query.get_or_404(ticketId=id).first()
        if ticked_q is not None:
            ticked_q.taskId = data['task_Id']
            ticked_q.title = data['title']
            ticked_q.body = data['body']
            ticked_q.TicketType = data['TicketType']
            ticked_q.user_id = user_id
            ticked_q.role = role

            db.session.commit()
            return jsonify({}), 200
        else:
            return jsonify({}), 500

    if role == 1 or role == 2:
        ticked_q = Ticket.query.get_or_404(ticketId=id).first()

        if user_id != ticked_q.user_id:
            return jsonify({'forbidden': 'wrong user id'}), 403

        if ticked_q is not None:
            ticked_q.taskId = data['task_Id']
            ticked_q.title = data['title']
            ticked_q.body = data['body']
            ticked_q.TicketType = data['TicketType']
            ticked_q.user_id = user_id
            ticked_q.role = role

            db.session.commit()
            return jsonify({}), 200
        else:
            return jsonify({}), 500
