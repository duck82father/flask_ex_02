import os
from flask import Blueprint, render_template, url_for


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_world():
    return '헬로 월드!'

@bp.route('/')
def index():
    return render_template('index.html')
