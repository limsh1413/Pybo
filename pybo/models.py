from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pw = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    age = db.Column(db.String(2), nullable=False)
    birth = db.Column(db.String(8), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(150), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120),unique=True, nullable=False)
