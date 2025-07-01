from app import app, database
from flask import render_template, flash, redirect, url_for, jsonify, request
from app.forms import Formlogin, FormMorador, FormEncomenda, FormHistoricoEncomenda
from app.models import Usuario, Unidade, Morador, Encomenda
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os
from datetime import datetime, time
from collections import defaultdict

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

@app.route('/moradores-da-unidade/<int:unidade_id>')
@login_required
def moradores_da_unidade(unidade_id):
    moradores = Morador.query.filter_by(unidade_id=unidade_id).all()
    moradores_json = [{"id": m.id, "nome": m.nome} for m in moradores]
    return jsonify(moradores_json)

@app.route('/cadastra_encomenda', methods=['GET', 'POST'])
@login_required
def cadastra_encomenda():
    unidades = Unidade.query.all()

    if request.method == 'POST':
        morador_id = request.form.get('morador_id')
        nf = request.form.get('nf')
        porteiro = current_user.nome

        if not morador_id or not nf:
            flash("Todos os campos são obrigatórios!", "danger")
            return redirect(url_for('nova_encomenda'))

        encomenda = Encomenda(
            morador_id=int(morador_id),
            nf=nf,
            porteiro=porteiro,
            data_recebimento=datetime.now()
        )
        database.session.add(encomenda)
        database.session.commit()

        flash("Encomenda cadastrada com sucesso!", "success")
        return redirect(url_for('home'))
    
    return render_template('cadastra_encomenda.html', unidades=unidades)


@app.route('/encomendas_pendentes')
@login_required
def encomendas_pendentes():
    encomendas = Encomenda.query.filter_by(status='Pendente').all()
    hora = datetime.now()
    agrupadas = defaultdict(list)

    for encomenda in encomendas:
        chave = (encomenda.morador.unidade.numero, encomenda.morador.unidade.bloco)
        agrupadas[chave].append(encomenda)
    return render_template('baixa_encomenda.html', encomendas=encomendas, encomendas_agrupadas=agrupadas, hora=hora)


@app.route("/dar-baixa/<int:id>", methods=["GET", "POST"])
def dar_baixa_encomenda(id):
    encomenda = Encomenda.query.get(id)
    encomenda.status = "Entregue"
    encomenda.data_retirada = datetime.now()
    encomenda.retirado_por = request.form["retirado_por"]
    database.session.commit()
    flash("Encomenda baixada com sucesso!", "success")
    return redirect(url_for("encomendas_pendentes"))


@app.route('/historico_retirada', methods=['GET', 'POST'])
@login_required
def historico_retirada():
    form = FormHistoricoEncomenda()
    if form.validate_on_submit():
        dt_inicial = datetime.combine(form.data_inicial.data, time.min) 
        dt_final = datetime.combine(form.data_final.data, time.max) 
        encomendas = Encomenda.query.filter(Encomenda.data_retirada >= dt_inicial, Encomenda.data_retirada <= dt_final).all()
        return render_template('historico_retirada.html', form=form, encomendas=encomendas)
    return render_template('historico_retirada.html', form=form, encomendas=None)