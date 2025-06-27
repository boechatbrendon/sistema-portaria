from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import Formlogin
from app.models import Usuario
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Formlogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usuario and usuario.senha == form.senha.data:
            login_user(usuario)
            flash('Login realizado com sucesso', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario ou Senha, Invalido', 'error')
    return render_template('login.html', form = form)


@app.route('/')
@login_required
def home():
    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Usuário desconectado.', 'danger')
    return redirect(url_for('login'))