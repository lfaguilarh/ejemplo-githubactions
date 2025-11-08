from flask import Blueprint, render_template, session

dashboard = Blueprint('dashboard',__name__,template_folder='templates')

@dashboard.route('/dashboard', methods = ['GET'])
def index():
    return render_template('/dashboard.html', user = session['user'])