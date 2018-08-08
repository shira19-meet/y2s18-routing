from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)



@app.route('/')
def home():
    return render_template(
    	'home.html')

@app.route('/<int:student_id>')
def display_student(student_id):
	student =query_by_id(student_id)
	return render_template(
    	'student.html' ,s=student_id, n=student.name, y=student.year, f=student.finished_lab)







app.run(debug=True)
