from flask import render_template, redirect, url_for

from app import app, db
from app.forms import URLForm
from app.models import URLmodel
from app.utils import get_short


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = URLmodel()
        url.original_url = form.original_url.data
        url.short = get_short()
        db.session.add(url)
        db.session.commit()
        return redirect(url_for('urls'))
    return render_template('index.html', form=form)


@app.route('/urls')
def urls():
    return render_template('urls.html', urls=URLmodel.query.all())


@app.route('/<string:short>')
def url_redirect(short):
    url = URLmodel.query.filter(URLmodel.short == short).first()
    if url:
        url.visits += 1
        db.session.add(url)
        db.session.commit()
        return redirect(url.original_url)
    return redirect(url_for('index'))
