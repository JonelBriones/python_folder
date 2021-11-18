from flask import Flask, render_template
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/table')
def hello_world():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

    # Return the string 'Hello World!' as a response
    return render_template("index.html", names=users)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
