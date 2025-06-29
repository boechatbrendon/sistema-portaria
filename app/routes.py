from app import app, database
from flask import render_template, flash, redirect, url_for
from app.forms import Formlogin, FormMorador
from app.models import Usuario, Unidade, Morador
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os


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

def salvar_foto(arquivo):
    nome_seguro = secure_filename(arquivo.filename)
    caminho = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], nome_seguro)
    arquivo.save(caminho)
    return nome_seguro

def limpar_mascara(input):
    input = ''.join(filter(str.isdigit, input))
    return input

@app.route('/cadastro_morador', methods=['GET', 'POST'])
@login_required
def cadastro_morador():
    form = FormMorador()
    unidades = Unidade.query.all()

    form.unidade.choices = [(u.id, f'{u.numero} - Bloco {u.bloco}') for u in unidades]

    if form.validate_on_submit():
        celular = limpar_mascara(form.celular.data)
        cpf = limpar_mascara(form.cpf.data)

        if form.foto.data:
            foto_morador = salvar_foto(form.foto.data)
            morador = Morador(
            nome=form.nome.data,
            cpf=cpf,
            email=form.email.data,
            celular=celular,
            unidade_id=form.unidade.data,
            foto=foto_morador
        )
        else:
            morador = Morador(
            nome=form.nome.data,
            cpf=cpf,
            email=form.email.data,
            celular=celular,
            unidade_id=form.unidade.data
        )
        database.session.add(morador)
        database.session.commit()
        flash("Morador cadastrado com sucesso", "success")
        return redirect(url_for('home'))


    return render_template('cadastro_morador.html', form = form)


@app.route('/unidades')
@login_required
def listar_unidades():
    unidades = Unidade.query.all()

    return render_template('unidades.html', unidades=unidades)


@app.route('/unidade/<int:id>')
@login_required
def moradores_unidade(id):
    unidade = Unidade.query.get(id)
    moradores = Morador.query.filter_by(unidade_id=id).all()
    return render_template('moradores_unidade.html', unidade=unidade, moradores=moradores)