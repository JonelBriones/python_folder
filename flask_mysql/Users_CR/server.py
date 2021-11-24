
from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)


@app.route('/new')
def new():
    return render_template("new.html")


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


@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)


if __name__ == "__main__":
    app.run(debug=True)
