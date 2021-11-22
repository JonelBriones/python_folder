from flask import Flask, render_template, request, redirect, session  # added request
app = Flask(__name__)
# our index route will handle rendering our form
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    # session.clear()
    return render_template("index.html")


@app.route('/survey', methods=["POST"])
def survey():
    session['user_name'] = request.form['name']
    # session['user_location'] = request.form['location']
    # session['user_langauge'] = request.form['langauge']
    # session['user_comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
