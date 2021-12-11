from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app


@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/create')

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date": request.form['date'],
        "time": request.form['time'],
        "user_id": session['user_id']
    }
    Recipe.save(data)
    return redirect('/dashboard')


@app.route('/view/<int:recipe_id>')
def view(recipe_id):

    if 'user_id' not in session:
        return redirect('/home')

    data = {
        "id": session['user_id']
    }
    recipe_data = {
        "id": recipe_id
    }
    return render_template("view.html", user=User.get_one(data), recipe=Recipe.get_recipe(recipe_data))


@app.route('/update_process/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    update_data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date": request.form['date'],
        "time": request.form['time'],
        "id": recipe_id,
    }
    Recipe.update(update_data)
    return redirect("/dashboard")


@app.route('/delete/<int:recipe_id>')
def delete(recipe_id):
    data = {
        "id": recipe_id
    }
    Recipe.delete(data)
    return redirect('/dashboard')
