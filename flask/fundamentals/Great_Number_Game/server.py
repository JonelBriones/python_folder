# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key = 'Keep it secreat, keep it safe'


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def guess():
    if 'guess' == 4 in session:
        return render_template('Correct.html')
    else:
        return render_template('index.html')


@app.route('/guess', methods=['POST'])
def test():
    if 'guess' in session:
        if request.form['guess'] == 4:
            return redirect('/show')
    return redirect('/show')


@app.route('/show')
def show():
    if session['guess'] == 4:
        return render_template('Low.html')
    return render_template('tryagain.html')


@app.route('/clear')
def clear():
    session.clear()
    return


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
