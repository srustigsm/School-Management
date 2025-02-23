from flask import Blueprint, render_template

headmaster = Blueprint('headmaster', __name__)

@headmaster.route('/dashboard')
def dashboard():
    return render_template('headmaster.html')
