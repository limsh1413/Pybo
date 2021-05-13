from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect

from pybo.form import NaverbookForm, NavermovieForm
from pybo.naverapi import naverbook, navermovie

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book/', methods=('GET','POST'))
def book():
    form = NaverbookForm()
    if request.method == "POST" and form.validate_on_submit():
        result = naverbook(form.search.data)
        return render_template('naver/naverbook.html',bookinfo_list=result['items'],form=form)


    return render_template('naver/naverbook.html', form=form)

@bp.route('/movie/', methods=('GET','POST'))
def movie():
    form = NavermovieForm()
    if request.method == "POST" and form.validate_on_submit():
        result = navermovie(form.search.data)
        return render_template('naver/navermovie.html',movierank_list=result['items'],form=form)


    return render_template('naver/navermovie.html', form=form)



