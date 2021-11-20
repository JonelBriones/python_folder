from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Keep it secreat, keep it safe'

# our index route will handle rendering our form


@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html")


@app.route('/reset')
def counting():
    session.clear()
    return redirect('/')


# @app.route('/process', methods=['GET', 'POST'])
# def clicked():
#     print("clicked")
#     print(request.form['click'])
#     session['click'] = request.form['click']
#     return redirect('/counter')


# @app.route('/counter')
# def counter():
#     count = 0
#     count += 1
#     print(count)
#     return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
