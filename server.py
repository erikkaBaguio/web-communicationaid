from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from models import *
from flask_cors import CORS
import json
import os

server = Flask(__name__)


@server.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':

        user = Account.query.filter_by(username=request.form['username']).first()

        if user is None:
            flash('Username or password invalid!')
            return redirect(url_for('login'))
        else:
            if check_password_hash(user.password_hash, request.form['password']):
                session['user'] = user.username
                session['fname'] = user.firstname
                session['role'] = user.acc_type

                if session['role'] == '2':
                    return redirect(url_for('teacher_landing'))
                elif session['role'] == '1':
                    return redirect(url_for('parent_landing'))

    return render_template("login.html")

@server.route('/logout')
def logout():
    if session['user'] is None:
        return redirect(url_for('login'))
    else:
        session.pop('user')
        session.pop('fname')
        session.pop('role')
        return redirect(url_for('login'))



@server.route('/register', methods=['GET','POST'])
def register():
    return render_template("SignUp.html")


@server.route('/teacher', methods=['GET','POST'])
def teacher():
    return render_template("teacher.html")

# @server.route('//view_students')
# def view_students():
#     if 'user' in session and session['role'] == '2':
#         return render_template('view_students.html')
#     else:
#         flash('You are not logged in! Please log in below!')
#         return render_template('login.html')

@server.route('/manageclass')
def manageclass():
    if 'user' in session and session['role'] == '2':
    manageclass = Class.query.order_by(Class.class_name).all()
    return render_template('class.html', manageclass=manageclass)


@server.route('/classPage/<class_name>')
def classPage(class_name):
    classes = Class.query.filter_by(class_name=class_name).first()
    students = Child.query.filter_by(c_id=Child.c_id).all()
    return render_template('classPage.html', Class=classes, students=students)   

@app.route('/students')
def students():
    if 'user' in session and session['role'] == '2':
    students = Child.query.order_by(Child.c_id).all()
    return render_template('students.html', Child=students)


@server.route('/addClass')
def addClass():
    if 'user' in session and session['role'] == '2':
        return render_template('addClass.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login.html')

@server.route('/addstudent')
def addstudent():
    if 'user' in session and session['role'] == '2':
        return render_template('addstudent.html')
    else:
        flash('You are not logged in! Please log in below!')
        return render_template('login.html')

@server.route('/manageclass')
def manageclass():
    if 'user' in session and session['role'] == '2':
        return render_template('manageclass.html')

# ################################################################

# @server.route('/manageclass')
# def manageclass():
#     manageclass = Class.query.order_by(Class.class_name).all()
#     return render_template('class.html', manageclass=manageclass)


# ################################################################    


# @server.route('/addClass', methods=['POST', 'GET'])
# def addClass():

#     if request.method == 'POST':
#         classes = Class(Class.class_name)
#         classes.class_name = request.form['class_name']


#         classes = db.session.merge(classes)
#         db.session.add(classes)
#         db.session.commit()
#         return redirect(url_for('manageclass', classes=classes))
#     else:
#         return render_template('addclass.html')


# ################################################################


# @server.route('/deleteClass/<class_num>', methods=['POST', 'GET'])
# def deleteClass(class_num):
#     class_ = Class.query.filter_by(class_num=class_num).first()
#     print class_
#     class_ = db.session.merge(class_)
#     db.session.delete(class_)
#     db.session.commit()
#     return redirect(url_for('manageclass'))


# ################################################################


# @server.route('/classPage/<class_name>')
# def classPage(class_name):
#     classes = Class.query.filter_by(class_name=class_name).first()
#     students = Child.query.filter_by(c_id=Child.c_id).all()
#     return render_template('classPage.html', Class=classes, students=students)


# ################################################################


# @server.route('/students')
# def students():
#     students = Child.query.order_by(Child.c_id).all()
#     return render_template('students.html', Child=students)


# ################################################################


# @server.route('/addstudents', methods=['POST', 'GET'])
# def addstudents():
#     if request.method == 'POST':

#         #student = Child(Child.c_id).first()
#         student = Child(fname_c=request.form['fname_c'], lname_c=request.form['lname_c'], bday_c=None, diagnosis=None)
#         #student.c_id = request.form['c_id']
#         #student.fname_c = request.form['fname_c']
#         #student.lname_c = request.form['lname_c']


#         #student = db.session.merge(student)
#         db.session.add(student)
#         db.session.commit()
#         return redirect(url_for('students', student=student))
#     else:
#         ch = Child.query.order_by(Child.c_id.desc()).first()
#         d = 1
#         if ch:
#             d = int(ch.c_id) + 1

#         return render_template('addstudent.html', d=d)
     

# ################################################################


# @server.route('/deletestudent/<c_id>', methods=['POST', 'GET'])
# def deletestudent(c_id):
#     students = Child.query.filter_by(c_id=c_id).first()
#     students = db.session.merge(students)
#     db.session.delete(students)
#     db.session.commit()

#     students_0 = Child.query.order_by(Child.c_id).all()
#     return redirect(url_for('students', students=students_0))


################################################################

CORS(server)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/communicationaid'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dc = SQLAlchemy(server)
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)


if __name__=='__main__':
    server.run(host='localhost', port=8000, debug=True)