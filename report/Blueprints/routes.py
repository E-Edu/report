from flask import Blueprint, render_template, abort,request, jsonify
from jinja2 import TemplateNotFound

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

@main_page.route('/ticket/delete/<id>')
def ticked_delete(id):
    return "hello World"

@main_page.route('/ticket/list')
def ticked_list():
    return "hello World"

@main_page.route('/ticket/edit')
def ticked_edit():
    return "hello World"
