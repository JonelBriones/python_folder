from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play1():
    # notice the 2 new named arguments!
    return render_template("index.html", num=3, color="cyan")


@app.route('/play/<int:num>')
def play2(num):
    # notice the 2 new named arguments!
    return render_template("index.html", num=num, color="cyan")


@app.route('/play/<int:num>/<string:color>')
def play3(num, color):
    # notice the 2 new named arguments!
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
