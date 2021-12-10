from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app.models.user import User
from flask_app.models.login import Login


@app.route('/create_message', methods=['POST'])
def create_message():

    # sender_id = user_id

    data = {
        "sender_id": session['user_id'],
        "receiver_id": request.form['receiver.id'],
        "message": request.form['message'],
    }
    Message.save(data)

    return redirect('/dashboard')


@app.route('/delete_message/<int:id>')
def delete_message(id):
    data = {
        "id": id
    }
    print(data)
    # Message.get_my_messages(data)
    Message.delete_message(data)
    return redirect('/dashboard')
