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
    if all(key in data for key in ('session', 'task_id','title','body','TicketType')): 
        print("Works")
    else:
        return jsonify({'error':'Missing Keys'}),510

    print(data)
    return "hello World"

@main_page.route('/ticket/delete/<id>', methods=['DELETE'])
def ticked_delete(id):
    ticket = Ticket.query.get(id)
    db.session.delete(ticket)
    db.session.commit()

@main_page.route('/ticket/list')
def ticked_list():
    return "hello World"

@main_page.route('/ticket/edit')
def ticked_edit():
    return "hello World"
