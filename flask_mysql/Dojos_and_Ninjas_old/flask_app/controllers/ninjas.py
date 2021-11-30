from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja


@app.route('/create_ninja/process', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["location"],
    }
    Ninja.save(data)
    return redirect('/')
