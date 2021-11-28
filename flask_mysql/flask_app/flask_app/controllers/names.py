from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.name import Name

# burgers.py...
from flask_app.models.name import Name
# gets all the burgers and returns them in a list of burger objects .


@app.route('/')
def burgers():
    return render_template('index.html', burgers=Name.get_all())
