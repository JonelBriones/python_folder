from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    # session.clear()
    return render_template("index.html")


@app.route('/survey', methods=['POST'])
def survey():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    Dojo.save(data)
    return redirect('/result')


@app.route('/result')
def result():
    all_dojos = Dojo.get_all()
    return render_template("result.html", all_dojos=all_dojos)
