from flask import url_for, request
from nutritiontracker import app
from nutritiontracker.models import User

# @app.route('/login', methods = ['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_in_user(request.form['username'])
#         else:
#             error  = 'Invalid username/password'
#     return render_template('login.html', error = error)


@app.route('/home/<int:id>', methods = ['POST', 'GET'])
def homeSearch(id):
    error = None
    if request.method == 'POST':
        pass