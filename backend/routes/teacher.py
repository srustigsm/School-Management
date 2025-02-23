from flask import Blueprint, render_template

teacher = Blueprint('teacher', __name__)

@teacher.route('/dashboard')
def dashboard():
    return render_template('teacher.html')
