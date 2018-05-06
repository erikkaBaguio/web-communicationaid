from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory, session
from sqlalchemy import *
from model import Parent, Child, Account, Teacher, db
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# for viewing of pages purposes

@app.route('/')
def parent_mode():
    # session['user'] = 'me'
    return render_template('p_mode.html')

@app.route('/child_class')
def child_class():
    # session['user'] = 'me'
    return render_template('c_class.html')

@app.route('/categories_list')
def list_categories():
    return render_template('l_categories.html')

@app.route('/edit_mode')
def e_mode():
    return render_template('edit_mode.html')

@app.route('/child_activity')
def c_act():
    return render_template('c_act.html')

@app.route('/child_prof')
def c_prof():
    return render_template('c_prof.html')

@app.route('/parent_prof')
def p_prof():
    return render_template('p_prof.html')

@app.route('/directory')
def directory():
    return render_template('directory.html')