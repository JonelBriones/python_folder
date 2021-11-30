from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja


# to add a ninja
@app.route('/dojo/create_ninja/process', methods=['POST'])
def create_ninja_process():
    print(request.form)
    data = {

        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo.id'],
    }
    Ninja.save(data)
    return redirect('/dojo')
