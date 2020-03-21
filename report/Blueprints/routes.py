from flask import Blueprint, render_template, abort,request, jsonify
from jinja2 import TemplateNotFound
from report.database import Ticket
from report import db

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
        return jsonify({'error':'Missing Keys'}),510

    try:
        userdata = jwt.decode(data['session'],os.environ.get('JWT_SECRET') , algorithms=['ES256'])
    except Exception as e:
        return jsonify({'error':'Invalid Session'}),510
    
    
    return "hello World"

@main_page.route('/ticket/delete/<id>', methods=['DELETE'])
def ticked_delete(id):


    session_allow = True

    if session_allow:
        ticket = Ticket.query.get(id)
        db.session.delete(ticket)
        db.session.commit()

@main_page.route('/ticket/list')
def ticked_list():
    return "hello World"

@main_page.route('/ticket/edit')
def ticked_edit():
    return "hello World"
