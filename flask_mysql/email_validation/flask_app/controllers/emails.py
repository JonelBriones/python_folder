from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.email import Email

# redirect to main template


@app.route('/')
def emails():
    return render_template('index.html', all_emails=Email.get_all())

# on submit will POST and retrieve back all emails


@app.route('/register', methods=['POST'])
def validate():
    if not Email.validate_user(request.form):
        return redirect('/')

    data = {
        "email": request.form['email']
    }
    print("saving")
    Email.save(data)

    return redirect("/success")


@app.route('/success')
def success():
    Email.success()
    return render_template("success.html", all_emails=Email.get_all())
