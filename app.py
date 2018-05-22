from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import Class, Child, Account, Teacher, db
from flask_cors import CORS
import json
import os

app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_SESSION_FOR_NEXT'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'thisissecret'
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

def createDB():
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:password@localhost/comm') #connects to server
    conn = engine.connect()
    conn.execute("commit")
    #engine.execute("CREATE DATABASE IF NOT EXISTS sample") #create db
    #engine.execute("USE sample") # select new
    conn.execute("create database communicationaid")
    conn.close()

def createTables():
    db.create_all()

################################################################


@app.route('/')
def teacher():
    return render_template('teacher.html')



################################################################    

@app.route('/manageclass')
def manageclass():
    manageclass = Class.query.order_by(Class.class_name).all()
    return render_template('class.html', manageclass=manageclass)


################################################################    


@app.route('/addClass', methods=['POST', 'GET'])
def addClass():

    # if request.method == 'POST':
    #     if request.form['class_name']!="":
    #         classes = Class(Class.class_name)

    #         classes.class_name = request.form['class_name']


    #         classes = db.session.merge(classes)
    #         db.session.add(classes)
    #         db.session.commit()
    #         return redirect(url_for('manageclass'))
    #     return render_template('addclass.html')
    # else:
        return render_template('addclass.html')


################################################################


@app.route('/deleteClass/<class_name>')
def deleteClass(class_name):
    class_name = Class.query.filter_by(class_name=class_name).first()
    print class_name
    class_name = db.session.merge(class_name)
    db.session.delete(class_)
    db.session.commit()
    return redirect(url_for('manageclass'))


###############################################################


@app.route('/classPage/<class_name>')
def classPage(class_name):
    classes = Class.query.filter_by(class_name=class_name).first()
    students = Child.query.filter_by(c_id=Child.c_id).all()
    return render_template('classPage.html', Class=classes, students=students)


################################################################


@app.route('/students')
def students():
    students = Child.query.order_by(Child.c_id).all()
    return render_template('students.html', Child=students)


################################################################


@app.route('/addstudents', methods=['POST', 'GET'])
def addstudents():
    # if request.method == 'POST':
    #     if request.form['fname_c']!="" and request.form['lname_c']!="": 
    #         student = Child(fname_c=request.form['fname_c'], lname_c=request.form['lname_c'], bday_c=None, diagnosis=None)

    #         db.session.add(student)
    #         db.session.commit()
    #         return redirect(url_for('students', student=student))
    return render_template('addstudent.html')
    # else:
    #     ch = Child.query.order_by(Child.c_id.desc()).first()
    #     d = 1
    #     if ch:
    #         d = int(ch.c_id) + 1    

    #     return render_template('addstudent.html', d=d)
     

################################################################

@app.route('/deletestudent/<c_id>', methods=['GET', 'POST'])
def deletestudent(c_id):
    students = Child.query.filter_by(c_id=c_id).first()
    students = db.session.merge(students)
    print students
    db.session.delete(students)
    db.session.commit()
    return redirect(url_for('students'))

################################################################

# @app.route('/deletestudent/<c_id>', methods=['POST', 'GET'])
# def deletestudent(c_id):
#     students = Child.query.filter_by(c_id=c_id).first()
#     students = db.session.merge(students)
#     db.session.delete(students)
#     db.session.commit()

#     students_0 = Child.query.order_by(Child.c_id).all()
#     return redirect(url_for('students', students=students_0))


################################################################



if __name__ == "__main__":
    app.run(debug=True)