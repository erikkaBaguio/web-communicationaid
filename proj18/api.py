from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import *
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
import account
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost/db'
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

import account

@app.route('/api/signup', methods=['POST'])
def createuser():
    print 'earl1'
    #data = request.get_json()
    print request.args.get('username')
    print request.args.get('email')
    print request.args.get('password')
    print request.args.get('acc_type')

    hashed_password = generate_password_hash(request.args.get('password'), method='sha256')
    new_acc = Account(acc_type=int(request.args.get('acc_type')), username=request.args.get('username'), email=request.args.get('email'),
                      password=hashed_password)

    db.session.add(new_acc)
    db.session.commit()

    print 'earl2'
    if request.args.get('acc_type'):
        new_acc = Account.query.filter_by(acc_type=int(request.args.get('acc_type'))).order_by(desc(acc_id)).all()
        if int(request.args.get('acc_type')) == 1:
            teacher_or_parent = Teacher(fname_t=None, lname_t=None, bday_t=None, specialty=None, tel_num=None,
                                        add_t=None, acc_id=new_acc.acc_id)
        else:
            teacher_or_parent = Parent(fname_p=None, lname_p=None, bday_p=None, add_p=None, acc_id=new_acc.acc_id)

    db.session.add(teacher_or_parent)
    db.session.commit()

    print 'earl3'
    return jsonify({'message': 'New user created.'})

if __name__ == "__main__":
    app.run(threaded=True, port=8080)