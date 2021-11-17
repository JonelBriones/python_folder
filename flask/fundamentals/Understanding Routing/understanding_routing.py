from flask import Flask, render_template


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# The "@" decorator associates this route with the function immediately following


@app.route('/dojo')
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response


@app.route('/say/<name>')
def hi(name):
    # Return the string 'Hello World!' as a response
    # return 'Hi' + ' ' + name.capitalize() + '!'
    return f"Hi {name.capitalize()}!"


@app.route('/repeat/<int:num>/<string:value>')
def repeat(value, num):
    return f"{num * value}"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
