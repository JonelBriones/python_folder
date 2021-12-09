from flask_app.models.user import User
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

############ Register ###########


@app.route('/')
def burgers():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template('index.html', users=User.get_all())


@app.route('/register', methods=['POST'])
def register():
    # will flash a message if request is invalid
    if not User.validate_register(request.form):
        return redirect('/')
    # if statement to confirm password matches
    if request.form['password'] == request.form['cpassword']:
        pw_hash = bcrypt.generate_password_hash(request.form['cpassword'])
        print(pw_hash)
        data = {
            "fname": request.form['fname'],
            "lname": request.form['fname'],
            "email": request.form['email'],
            "password": pw_hash
        }
        # will only save from data if password is confirmed
        user_id = User.save(data)
        session['user_id'] = user_id
    return redirect('/login')
