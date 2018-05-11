from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from app import app
import os
from werkzeug.security import generate_password_hash, check_password_hash
import sys, flask, requests
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from SimpleHTTPServer import SimpleHTTPRequestHandler, test
# from requests.auth import HTTPBasicAuth


@app.route('/')
@cross_origin(origin='*')
def index():
	

	return render_template('welcome.html')

# @app.route('/login', methods=['POST'])
# @cross_origin(origin='*')
# def login():
# 	username = request.form['username']
# 	password = request.form['password']
# 	r = requests.post('https://mighty-badlands-16603/api/login', auth=HTTPBasicAuth('user', 'pass'), json = {'username':name, 'password':password})
# 	return r
@app.route('/mode/<acc_id>', methods=['GET'])
def mode(acc_id):

	return render_template('mode.html')
@app.route('/signup', methods=['GET'])
def signup():

	return render_template('registration.html')

@app.route('/parent')
@cross_origin(origin='*')
def parent():
  return render_template('p_prof.html')

@app.route('/class/add', methods=['GET'])
def addclass():
	return render_template('class.html')


@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

