from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    return render_template('index.html')


@bp.route('/page1')
def page1():
    return render_template('page1.html')


@bp.route('/page2')
def page2():
    return render_template('page2.html')


@bp.route('/page3')
def page3():
    return render_template('page3.html')
