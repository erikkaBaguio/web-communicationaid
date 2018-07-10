from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, url_for,redirect,send_from_directory
from app import app
import requests
import os
from werkzeug.security import generate_password_hash, check_password_hash
import sys, flask, requests
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from SimpleHTTPServer import SimpleHTTPRequestHandler, test


@app.route('/')
def index():
	return render_template('welcome.html')

@app.route('/mode/<int:acc_id>', methods=['GET'])
def mode(acc_id):
	return render_template('mode.html')

@app.route('/register', methods=['GET'])
def signup():
	return render_template('registration.html')

@app.route('/login', methods=['GET'])
def login():
	return render_template('login.html')

@app.route('/parent/profile/<int:acc_id>')
def parent(acc_id):
	req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/get_pprof/"+str(acc_id))
	data = req.json()
	name = data['fname_p'] +" "+ data['lname_p']
	img = data['img']
	gender = data['gender_p']
	bday = data['bday_p']
	bio = data['bio_p']
	mail = data['email']
	address = data['add_p']

	return render_template('ParentProfile.html',name=name,bday=bday,img=img,gender=gender,bio=bio,email=mail,address=address)

@app.route('/child/profile/<int:acc_id>')
def child(acc_id):

	try:

		req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/get_cprof/"+str(acc_id))
		data = req.json()
		name = data['fname_c'] +" "+ data['lname_c']
		img = data['img']
		gender = data['gender']
		bday = data['bday_c']
		classes = data['classes']
		diagnosis = data['diagnosis']

		return render_template('ChildProfile.html',classes=classes,name=name,img=img,gender=gender,bday=bday,diagnosis=diagnosis)

	except:
		return render_template('pchild_upload.html')


@app.route('/personalinfo/parent/<acc_id>')
def parentinfo(acc_id):
	return render_template("edit_p.html")

@app.route('/personalinfo/teacher/<acc_id>')
def teacherinfo(acc_id):
	return render_template("edit_t.html")

@app.route('/personalinfo/child/<acc_id>')
def childinfo(acc_id):
	return render_template("edit_c.html")

@app.route('/dashboard/parent/<int:acc_id>')
def parentdashboard(acc_id):
	req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/get_pprof/"+str(acc_id))
	data = req.json()
	name = data['fname_p'] +" "+ data['lname_p']
	img = data['img']

	return render_template('index.html',img=img,name=name)

@app.route('/whoweare')
def whoweare():
  return render_template('team.html')

@app.route('/welcometopic-a-talk')
def logout():
  return render_template('welcome.html')

@app.route('/dashboard/child/<int:acc_id>')
def childdashboard(acc_id):
  return render_template('navigation.html')

@app.route('/class/add/<int:acc_id>', methods=['GET'])
def addclass(acc_id):
	return render_template('class.html')

@app.route('/forum/<int:acc_id>', methods=['GET'])
def forum(acc_id):
	try:
		req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/get_pprof/"+str(acc_id))
		data = req.json()
		name = data['fname_p'] +" "+ data['lname_p']
		img = data['img']
		gender = data['gender_p']
		bday = data['bday_p']
		bio = data['bio_p']
		mail = data['email']
		address = data['add_p']

		return render_template('forum.html',name=name,bday=bday,img=img,gender=gender,bio=bio,email=mail,address=address)

	except:
		req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/teacherinfo/"+str(acc_id))
		data = req.json()
		name = data['fname_t'] +" "+ data['lname_t']
		img = data['img']
		specialty = data['specialty']
		bday = data['bday_t']
		bio = data['bio_t']
		mail = data['email']
		address = data['add_t']
		tel_num = data['tel_num']
		return render_template('forum.html',name=name,bday=bday,img=img,specialty=specialty,bio=bio,email=mail,address=address,num=tel_num)

@app.route('/educational/alphabets/<int:acc_id>', methods=['GET'])
def alphabet(acc_id):
	return render_template('ed_alphabet.html')

@app.route('/educational/shapes/<int:acc_id>', methods=['GET'])
def shapes(acc_id):
	return render_template('ed_shapes.html')

@app.route('/educational/colors/<int:acc_id>', methods=['GET'])
def colors(acc_id):
	return render_template('ed_colors.html')

@app.route('/educational/numbers/<int:acc_id>', methods=['GET'])
def numbers(acc_id):
	return render_template('ed_numbers.html')

@app.route('/directory/<int:acc_id>', methods=['GET'])
def directory(acc_id):
	return render_template('directory.html')

@app.route('/activitylogs/<int:acc_id>')
def actlogs(acc_id):
	return render_template('activityLog.html')

@app.route('/activitylogs/report_details')
def reportlogs():
	return render_template('report_details.html')

@app.route('/activitylogs/report_details2')
def reportlogs2():
	return render_template('report_details2.html')

@app.route('/teacher/profile/<int:acc_id>')
def teacherprof(acc_id):
	req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/teacherinfo/"+str(acc_id))
	data = req.json()
	name = data['fname_t'] +" "+ data['lname_t']
	img = data['img']
	specialty = data['specialty']
	bday = data['bday_t']
	bio = data['bio_t']
	mail = data['email']
	address = data['add_t']
	tel_num = data['tel_num']
	return render_template('TeacherProfile.html',name=name,bday=bday,img=img,specialty=specialty,bio=bio,email=mail,address=address,num=tel_num)


@app.route('/parent/profile/<int:acc_id>')
def parentprof(acc_id):
	return render_template('temporaryprofile.html')

@app.route('/child/progress/<int:acc_id>')
def childprogress(acc_id):
	return render_template('c_progress.html')

@app.route('/child/progress2/<int:acc_id>')
def childprogress2(acc_id):
	return render_template('c_progress2.html')

@app.route('/child/profile/<int:acc_id>')
def childprof(acc_id):
	return render_template('ChildProfile.html')

@app.route('/classPage/<string:class_name>')
def claz(class_name):
	return render_template('classPage.html')

@app.route('/classes/<int:acc_id>')
def classes(acc_id):
	return render_template('class.html')
@app.route('/clothes')
def clothes():
	return render_template('clothes.html')

@app.route('/clothes_b')
def clothes_b():
	return render_template('clothes_b.html')

@app.route('/clothes_g')
def clothes_g():
	return render_template('clothes_g.html')

@app.route('/places')
def places():
	return render_template('places.html')

@app.route('/toys')
def toys():
	return render_template('toys.html')

@app.route('/food')
def food():
	return render_template('food.html')

@app.route('/educational/<int:acc_id>')
def educational(acc_id):
	return render_template('educational.html')

@app.route('/dashboard/teacher/<int:acc_id>')
def teacherdashboard(acc_id):

	req = requests.get("https://cryptic-fjord-60133.herokuapp.com/api/teacherinfo/"+str(acc_id))
	data = req.json()
	name = data['fname_t'] +" "+ data['lname_t']
	img = data['img']
	return render_template('teacher_dashboard.html',name=name,img=img)

@app.route('/parent/profile/edit/<int:acc_id>')
def parentedit(acc_id):
	return render_template('edit_p.html')

@app.route('/child/profile/edit/<int:acc_id>')
def childedit(acc_id):
	return render_template('edit_c.html')

@app.route('/teacher/profile/edit/<int:acc_id>')
def teacheredit(acc_id):
	return render_template('edit_t.html')

@app.route('/progressreport/<int:acc_id>')
def report(acc_id):
	return render_template('report.html')

@app.route('/upload/<int:acc_id>')
def upload(acc_id):
	return render_template("upload_trial.html")

@app.route('/tprofilepic/<int:acc_id>')
def ppic(acc_id):
	return render_template("prof_upload.html")

@app.route('/pprofilepic/<int:acc_id>')
def parpic(acc_id):
	return render_template("prof_upload.html")

@app.route('/cprofilepic/<int:acc_id>')
def cpic(acc_id):
	return render_template('pchild_upload.html')

@app.route('/edit_categories/<int:acc_id>')
def edit_categories(acc_id):
	return render_template('categories.html')

@app.route('/categ/food/<int:acc_id>')
def categ_food(acc_id):
	return render_template('food.html')

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return render_template('error404.html'),404
