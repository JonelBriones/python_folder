# Import Flask to allow us to create our app
from flask import Flask, render_template, request, redirect, session
import random
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key = 'Keep it secreat, keep it safe'


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    # session.clear()
    if 'num' not in session:
        session['num'] = random.randint(1, 100)

    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
