from app import app
from flask import render_template, flash
from app.forms import Formlogin


@app.route('/', methods=['GET', 'POST'])
def login():
    form = Formlogin()
    if form.validate_on_submit():
        if form.usuario.data == 'porteiro' and form.senha.data == '123456':
            flash('Login realizado com sucesso', 'success')
        else:
            flash('Usuario ou Senha, Invalido', 'error')
    return render_template('login.html', form = form)