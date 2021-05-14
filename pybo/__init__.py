from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()


app = Flask(__name__)

# sqlalchmy db 설정
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

from . import models

from pybo.views import auth_views
from pybo.views import user_views
from pybo.views import naver_views
from pybo.views import main_views
from pybo.views import question_views
from pybo.views import answer_views
from pybo.views import movie_views
from .filter import format_datetime

app.jinja_env.filters['datetime']=format_datetime

app.register_blueprint(main_views.bp)
app.register_blueprint(naver_views.bp)
app.register_blueprint(user_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(movie_views.bp)