from app import app
from flask import render_template
from app.forms import Formlogin


@app.route('/', methods=['GET', 'POST'])
def login():
    form = Formlogin()

    return render_template('login.html', form = form)