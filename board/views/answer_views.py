from flask import Blueprint, request, url_for
from werkzeug.utils import redirect
from board.models import Question, Answer
from board import db

from datetime import datetime

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('create/<int:question_id>', methods=('post',))
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']
    answer = Answer(content=content, create_date=datetime.now())
    question.answer_set.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))