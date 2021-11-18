from flask import Flask, render_template
app = Flask(__name__)


@app.route('/checkboard')
def checkers():

    # notice the 2 new named arguments!
    return render_template("index.html", num=8)


@app.route('/checkboard/<int:num>')
def createboard(num):

    # notice the 2 new named arguments!
    return render_template("index.html", num=num)


# @app.route('/checkboard/<int:num>/<int:num2>')
# def xandy(num, num2):

#     # notice the 2 new named arguments!
#     return render_template("index.html", num=num, num2=num2)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
