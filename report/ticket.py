from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_page = Blueprint('simple_page', __name__, template_folder='templates')


@main_page.route('/')
def home():
    return "hello World"

@main_page.route('/ticket/create')
def ticked_create():
    return "hello World"

@main_page.route('/ticket/delete')
def ticked_delete():
    return "hello World"

@main_page.route('/ticket/list')
def ticked_list():
    return "hello World"

@main_page.route('/ticket/edit')
def ticked_edit():
    return "hello World"
