from flask import Blueprint
from pybo.models import user_info
from datetime import datetime
from pybo import db

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/hello')
def hello_pybo():
    q1= user_info(id=1,pw='비밀번호',name='김길동', phone='01012345678',age='25', birth='19970101', gender='M',
                  subject='회원가입하세요',content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q1)
    q2 = user_info(id=2, pw='비밀번호', name='길동', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q2)
    q3 = user_info(id=3, pw='비밀번호', name='동', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q3)
    q4 = user_info(id=4, pw='비밀번호', name='홍홍홍', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q4)
    q5 = user_info(id=5, pw='비밀번호', name='홍홍', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q5)
    q6 = user_info(id=6, pw='비밀번호', name='홍', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q6)
    q7 = user_info(id=7, pw='비밀번호', name='임금님', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q7)
    q8 = user_info(id=8, pw='비밀번호', name='임금', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q8)
    q9 = user_info(id=9, pw='비밀번호', name='금', phone='01012345678', age='25', birth='19970101', gender='M',
                   subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q9)
    q10 = user_info(id=10, pw='비밀번호', name='임', phone='01012345678', age='25', birth='19970101', gender='M',
                    subject='회원가입하세요', content='회원가입을 원합니다.', create_date=datetime.now())
    db.session.add(q10)

    db.session.commit()

    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'
