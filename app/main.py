from flask import Blueprint, render_template, request
from app import connect
from pprint import pprint

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    connection = connect()
    result = False
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('select * from posts', ())
            result = cursor.fetchall()

    return render_template('index.html', posts=result)


@bp.route('/calculate/buy', methods=['POST'])
def calculate_buy():
    return request.form


@bp.route('/page1')
def page1():
    return render_template('page1.html')


@bp.route('/page2')
def page2():
    return render_template('page2.html')


@bp.route('/page3')
def page3():
    return render_template('page3.html')
