from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def home():
    return render_template(
    	'home.html')

@app.route('/<int:student_id>')
def display_student(student_id):
	return render_template(
    	'student.html' ,s=student_id)
@app.route('/<int:student_name>')
def display_student(student_name):
	return render_template(
    	'student.html' ,n=student_name)
	@app.route('/<int:student_yaer>')
def display_student(student_year):
	return render_template(
    	'student.html' ,y=student_year)




app.run(debug=True)
