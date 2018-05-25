from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import *
from flask_cors import CORS
import json
import os

server = Flask(__name__)

@server.route('/TeacherProfile', methods=['GET','POST'])
def teacher():
    return render_template("TeacherProfile.html")

@server.route('/manageclass')
def manageclass():
      if 'user' in session and session['role'] == '1':
        manageclass = Class.query.order_by(Class.class_name).all()
        return render_template('class.html', manageclass=manageclass)
      else:
          flash('You are not logged in! Please log in below!')
          return render_template('login.html')
@server.route('/addClass', methods=['POST', 'GET'])
def addClass():
      if 'user' in session and session['role'] == '1':
        return render_template('manageclass.html')
      else:
          flash('You are not logged in! Please log in below!')
          return render_template('login.html')         

@server.route('/classPage/<class_name>')
def classPage(class_name):
      if 'user' in session and session['role'] == '1':
        classes = Class.query.filter_by(class_name=class_name).first()
        students = Child.query.filter_by(c_id=Child.c_id).all()
        return render_template('classPage.html', Class=classes, students=students)
      else:
          flash('You are not logged in! Please log in below!')
          return render_template('login.html')   

@app.route('/students')
def students():
      if 'user' in session and session['role'] == '1':
        students = Child.query.order_by(Child.c_id).all()
        return render_template('students.html', Child=students)
      else:
          flash('You are not logged in! Please log in below!')
          return render_template('login.html') 

@server.route('/addstudent', methods=['POST', 'GET'])
def addstudent():
      if 'user' in session and session['role'] == '1':
        return render_template('addstudent.html')
      else:
          flash('You are not logged in! Please log in below!')
          return render_template('login.html')


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
    server.run(host='localhost', port=5000, debug=True)