from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login import Login
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


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
    return redirect('/home')

######### LOGIN ##########


@app.route('/login', methods=['POST'])
def login():
    # validate data
    data = {
        "email": request.form['email']
    }
    user = Login.get_by_email(data)

    if not user:
        flash('Invalid email or password.', "login")
        return redirect('/home')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid email or password.', "login")
        return redirect('/home')
    session['user_id'] = user.id
    print("Logged in")
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/home')
    data = {
        "id": session['user_id']
    }
    get_all_users = User.get_all()
    get_messages = Message.get_my_messages(data)
    return render_template("login.html", user=User.get_one(data), get_all_users=get_all_users, get_messages=get_messages)


@app.route('/logout')
def logout():
    session.clear()

    # session.pop('user_id')
    return redirect("/home")


@app.route('/create_message', methods=['POST'])
def messages():
    data = {
        "user_id": session['user_id'],
        "message": request.form["message"]
    }
    Message.save(data)
    return redirect('/dashboard')
