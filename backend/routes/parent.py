from flask import Blueprint, render_template

parent= Blueprint('parent', __name__)

@parent.route('/dashboard')
def dashboard():
    return render_template('parent.html')
