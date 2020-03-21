from flask import Blueprint, render_template, abort,request, jsonify
from jinja2 import TemplateNotFound
from report.database import Ticket
from report import db
import jwt
import os

main_page = Blueprint('main-routes', __name__)


@main_page.route('/')
def home():
    return "hello World"

@main_page.route('/ticket/create', methods=['PUT'])
def ticked_create():
    data = request.json
    if data is not None and all(key in data for key in ('session', 'task_id','title','body','TicketType')): 
        print("Works")
    else:
        return jsonify({'error':'Missing Keys'}),400

    try:
        userdata = jwt.decode(data['session'],os.environ.get('JWT_SECRET') , algorithms=['ES256'])
    except Exception:
        return jsonify({'error':'INVALID_SESSION'}),400
    
    ticket = Ticket(data['task_id'],data['title'],data['body'],data['TicketType'])
    db.session.add(ticket)
    db.session.commit()
    return jsonify({}), 200

@main_page.route('/ticket/delete/<id>', methods=['DELETE'])
def ticked_delete(id):
    data = request.headers.get('session')
    try:
        userdata = jwt.decode(data['session'],os.environ.get('JWT_SECRET') , algorithms=['ES256'])
    except Exception:
        return jsonify({'error':'INVALID_SESSION'}),400
    
    ticket = Ticket.query.get(id)
    db.session.delete(ticket)
    db.session.commit()
    return jsonify({}), 200

@main_page.route('/ticket/list')
def ticked_list():
    return jsonify({}), 404


@main_page.route('/ticket/edit/<id>')
def ticked_edit(id):
    data = request.json
    if data is not None and all(key in data for key in ('session', 'task_id', 'title', 'body', 'TicketType')):
        print("Works")
    else:
        return jsonify({'error': 'Missing Keys'}), 510

    try:
        userdata = jwt.decode(data['session'], os.environ.get('JWT_SECRET'), algorithms=['ES256'])
    except Exception:
        return jsonify({'error': 'Invalid Session'}), 510
    ticked_q = Ticket.query.filter_by(ticketId=id).first()
    ticked_q.taskId = data['task_Id']
    ticked_q.title = data['title']
    ticked_q.body = data['body']
    ticked_q.TicketType = data['TicketType']
    db.session.commit()
    return jsonify({}), 200

