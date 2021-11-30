from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect('/dojo')

# dojo home and calls all dojos from database


@app.route('/dojo')
def dojo():
    return render_template('create_dojo.html', all_dojos=Dojo.get_all())

# to create new dojos


@app.route('/create_dojo/process', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form['dojo_name']
    }
    Dojo.save(data)
    return redirect('/dojo')


@app.route('/dojo/show/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    this_dojo = Dojo.get_dojo_and_ninjas(data)

    all_ninjas = Ninja.get_all()  # collects all ninjas
    return render_template('show_dojos_and_ninjas.html', this_dojo=this_dojo, all_ninjas=all_ninjas)


@app.route('/dojo/create_ninja')
def create_ninja():

    return render_template('create_ninja.html', all_dojos=Dojo.get_all())
