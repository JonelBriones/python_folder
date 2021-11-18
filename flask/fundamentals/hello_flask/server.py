from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # notice the 2 new named arguments!
    return render_template("index.html", phrase="hello", times=5)


# The "@" decorator associates this route with the function immediately following
# @app.route('/')
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes

# PLAYGROUND ASSIGNMENT


@ app.route('/success')
def success():
    return "success"
    # app.run(debug=True) should be the very last statement!


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@ app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@ app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
