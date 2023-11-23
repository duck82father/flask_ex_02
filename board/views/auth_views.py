# 필요한 것들
# - 플라스크 : 블루프린트, Url_for, Render_template, 플래쉬, 리퀘스트
# - 버크저그 : 패스워드 해쉬 발생기, 리다이렉트
# - db, Form(유저), Model(유저)

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from board import db
from board.forms import UserCreateForm, UserLoginForm
from board.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # 'None'이 'False'이면 = 기존에 존재하지 않는 유저라면!
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1),
                        email=form.email.data)
            db.session.add()
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        # 'None'이 'False'이면 = 기존에 존재하지 않는 유저라면!
        if not user:
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password, form.password.data):
            error = '비밀번호가 올바르지 않습니다.'
        if error in None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))