import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'lingualizer_alchemy.db'
DEBUG = True
SECRET_KEY = '2618f390726996e0e0226ca3a991c213'
USERNAME = 'admin'
PASSWORD = 'admin'
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# create app
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
import models
from forms import SegmentPrototypeForm

# routes
@app.route('/')
def index():
    """Segment_prototype list view."""
    segment_prototypes = db.session.query(models.SegmentPrototype)
    form = SegmentPrototypeForm()
    return render_template('index.html', segment_prototypes=segment_prototypes, form=form)

@app.route('/add', methods=['POST'])
def add_segment_prototype():
    """Adds new segment_prototype to the database."""
    if not session.get('logged_in'):
        abort(401)
    form = SegmentPrototypeForm()
    if form.validate_on_submit():
        new_segment_prototype = models.SegmentPrototype(
            form.ipa_group.data,
            form.ipa_name.data,
            form.ipa_symbol.data,
            form.ipa_manner.data,
            form.ipa_major_place.data,
            form.ipa_minor_place.data,
            form.ipa_voice.data,
            form.syllabic.data,
            form.consonantal.data,
            form.approximant.data,
            form.sonorant.data,
            form.voice.data,
            form.spread_glottis.data,
            form.constricted_glottis.data,
            form.continuant.data,
            form.nasal.data,
            form.strident.data,
            form.lateral.data,
            form.labial.data,
            form.round.data,
            form.coronal.data,
            form.anterior.data,
            form.distributed.data,
            form.dorsal.data,
            form.back.data,
            form.low.data,
            form.tense.data,
            form.radical.data,
            form.laryngeal.data,
            form.high.data
        )

        db.session.add(new_segment_prototype)
        db.session.commit()
        flash('New segment_prototype was successfully posted')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """User logout/authentication/session management."""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
