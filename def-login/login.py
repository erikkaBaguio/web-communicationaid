from flask import Flask, render_template, request, session, redirect, make_response, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import Account
from werkzeug.security import check_password_hash
from flask_cors import CORS
import os
server = Flask(__name__)


@server.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['login'] == 'Sign in':

            acc = Account.query.filter_by(username=request.form['username']).first()

            if acc is None:
                flash('Username or password is invalid!')
                return redirect(url_for('login'))
            else:
                if check_password_hash(acc.password_hash, request.form['password']):
                    session.pop('acc_id', None)
                    session.pop('acc_type', None)
                    session.pop('email', None)
                    # pops existing user data, if any!

                    session['acc_id'] = acc.acc_id
                    session['acc_type'] = acc.acc_type
                    session['email'] = acc.email

                    print session['user']

                    # if session['acc_type'] == 'Parent':
                    #     return redirect(url_for('landing_'parent))
                    # elif session['acc_type'] == 'Teacher':
                    #     return redirect(url_for('landing_teacher'))

    return render_template("login.html")

@server.route('/parent/landing', methods=['GET'])
def parent():
    if 'user' in session:
        if session['acc_type'] == 'Parent':
            return render_template("parent.html")
    else:
        flash('You are not logged in!')
        return render_template('login.html')


@server.route('/teacher/landing')
def teacher():
    if 'user' in session:
        if session['acc_type'] == 'Teacher':
            return render_template('teacher.html')
    else:
        flash('You are not logged in!')
        return render_template('login.html')

CORS(server)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:coycoy6197@localhost/test'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)

if __name__ == '__main__':
    server.run(host='localhost', port=8000, debug=True)