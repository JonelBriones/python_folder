from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route('/')
def home():
    return redirect('/dojo')


@app.route('/dojo')
def dojo():
    return render_template('create_dojo.html', all_dojos=Dojo.get_all())


@app.route('/create_ninja')
def ninja():
    return render_template('create_ninja.html', all_dojos=Dojo.get_all())


@app.route('/show_dojo_and_ninja/<int:dojo_id>')
def show(dojo_id):
    data = {
        "id": dojo_id,
    }
    this_dojo = Dojo.get_dojo_and_ninjas(data)  # passes data for ninjas
    return render_template('show_dojos_and_ninjas.html', this_dojo=this_dojo)


@app.route('/create_ninja/process', methods=['POST'])
def create_ninja():
    location = {
        "location": request.form["location"]
    }
    print(location)
    location = Dojo.get_dojo_id(location)
    print(Dojo.get_dojo_id(location))
    # data = {
    #     "fname": request.form["fname"],
    #     "lname": request.form["lname"],
    #     "age": request.form["age"],
    #     "id": location
    # }

    # Dojo.save_ninja(data)

    return redirect('/')
