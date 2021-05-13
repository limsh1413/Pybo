from flask import Blueprint,render_template,url_for
from pybo.models import Question,Answer
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/test')
def test():
    for i in range(100):
        q = Question(subject='테스트 데이터 [%03d]'%i, content='내용무', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()
    return redirect(url_for('main.index'))



@bp.route('/hello')
def main1():
    q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
    #result=Question.query.filter(Question.id==1).all()
    #result=Question.query.get(1)  # id(primary key) 1번 데이터를 가져옴
    #result=Question.query.filter(Question.subject.like('%무엇%')).all()
    #result=Question.query.filter(Question.username.like('%김%')).all()
    #print(result)
    #result.subject = '파이보 정말 재밌어요'
    #db.session.commit()
    #result=Question.query.get(1)
    #db.session.delete(result)
    #db.session.commit()


    # q = Question.query.get(5)
    #
    # a = Answer(question = q, content='답변 5번', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()
    #
    #
    # q=Question.query.get(5)
    # db.session.delete(q)
    # db.session.commit()


    #q = Question.query.get(2)

    # 2번 질문에 대한 답변 데이터를 가져오세요.
    # q = Question.query.get(5)
    # result=q.answer_set
    # print(result)

    # q=Question.query.get(2)
    # db.session.delete(q)
    # db.session.commit()

    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))