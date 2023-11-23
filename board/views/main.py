from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return '헬로 월드!'

@bp.route('/')
def index():
    return '홈'