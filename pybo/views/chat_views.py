from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from pybo.models import Question
from .. import db
from ..form import QuestionForm, AnswerForm, HelpForm
from werkzeug.utils import redirect
from pybo.dialogflowapi import chat

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')


@bp.route('/help/', methods=('GET','POST'))
def Help():
    form=HelpForm()
    if request.method == "POST" and form.validate_on_submit():
        result = chat(form.search.data,'1234')
        print(result)
        if result == '영화순위메뉴':
            return redirect(url_for('movie.Movierank'))
        elif result == '구글 가자':
            return redirect('http://www.google.com')

    return render_template('chat/help.html', form=form)