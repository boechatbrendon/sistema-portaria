from app import app
from flask import render_template, flash
from app.forms import Formlogin
from app.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def login():
    form = Formlogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usuario and usuario.senha == form.senha.data:
            flash('Login realizado com sucesso', 'success')
        else:
            flash('Usuario ou Senha, Invalido', 'error')
    return render_template('login.html', form = form)