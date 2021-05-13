from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.movieapi import Mrank

bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/rank/')
def Movierank():
    rankdata=Mrank()

    return render_template('movie/movierank.html', rdata=rankdata)