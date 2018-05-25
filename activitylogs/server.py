from flask import Flask, url_for, jsonify, request, render_template, send_from_directory, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from sqlalchemy import *
from model import *
from flask_cors import CORS
import json
import os

server = Flask(__name__)


@server.route('/activitylogs')
def activitylogs():
        return render_template('activityLog.html')


################################################################

CORS(server)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/comaid'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dc = SQLAlchemy(server)
server.config['USE_SESSION_FOR_NEXT'] = True
server.config['CORS_HEADERS'] = 'Content-Type'
server.config['SECRET_KEY'] = 'thisissecret'

server.secret_key = os.urandom(24)


if __name__=='__main__':
    server.run(host='localhost', port=5000, debug=True)