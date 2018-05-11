from flask import Flask, request,url_for, jsonify, render_template, make_response,session,Blueprint
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy, jwt, datetime, os


app = Flask(__name__)
server = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:walakokahibaw@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_SESSION_FOR_NEXT'] = True
app.config['SECRET_KEY'] = 'hard to guess string'


db = SQLAlchemy(app)
def createDB():
	engine = sqlalchemy.create_engine('postgresql://postgres:walakokahibaw@localhost/db')
	engine.execute("CREATE DATABASE IF NOT EXISTS communicationaid") 


def createTables():
	db.create_all()

