from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)


@app.route("/me")
def warehouse():
    name = "Michał"
    surname = "Bogoryja-Zakrzewski"
    return render_template("info.html", name=name, surname=surname)


@app.route('/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        mail = "m.michal.bz@gmail.com"
        phone = "501-501-501"
        return render_template("contact.html", mail=mail, phone=phone)
    elif request.method == 'POST':
        received_message = request.form
        print(f'''Recived message: {received_message['message']}''')
        return redirect("/contact")
