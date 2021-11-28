
from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)


@app.route('/new')
def new():
    return render_template("new.html")


@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
        "id": user_id,
    }
    user = User.get_one(data)
    return render_template("show.html", user=user)


@app.route('/process', methods=["POST"])
def process():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/update/<int:user_id>')
def update(user_id):
    data = {
        "id": user_id,
    }
    user = User.get_one(data)
    return render_template("edit.html", user=user)


@app.route('/update/<int:user_id>/process', methods=["POST"])
def update_process(user_id):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id": user_id,
        "fname": request.form["fname_update"],
        "lname": request.form["lname_update"],
        "email": request.form["email_update"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.update(data)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/show/{user_id}')


@app.route('/delete/<int:user_id>/process/yes', methods=["POST"])
def delete_yes(user_id):
    data = {
        "id": user_id,
    }
    User.delete(data)
    return redirect("/")


@app.route('/delete/<int:user_id>')
def delete_no(user_id):
    data = {
        "id": user_id,
    }
    user = User.get_one(data)
    return render_template('delete.html', user=user)


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)


if __name__ == "__main__":
    app.run(debug=True)
