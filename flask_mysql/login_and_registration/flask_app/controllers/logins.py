from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login import Login
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

######### LOGIN ##########


@app.route('/login', methods=['POST'])
def login():
    # validate data
    data = {
        "email": request.form['email']
    }
    user = Login.get_by_email(data)

    if not user:
        flash('Invalid email or password.')
        return redirect('/home')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid email or password.')
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
    return render_template("login.html", user=User.get_one(data))


@app.route('/logout')
def logout():
    session.clear()

    # session.pop('user_id')
    return redirect("/home")
