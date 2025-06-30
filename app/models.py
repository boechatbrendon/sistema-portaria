from app import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    usuario = database.Column(database.String, nullable=False)
    senha = database.Column(database.String, nullable=False)


class Unidade(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    numero = database.Column(database.String, nullable=False)
    bloco = database.Column(database.String, nullable=False)

    moradores = database.relationship('Morador', backref='unidade', lazy=True)


class Morador(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    cpf = database.Column(database.String(14), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    celular = database.Column(database.String(15), nullable=False)
    foto = database.Column(database.String, default='default.png')

    unidade_id = database.Column(database.Integer, database.ForeignKey('unidade.id'), nullable=False)


class Encomenda(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nf = database.Column(database.String(20), nullable=False)
    data_recebimento = database.Column(database.DateTime, nullable=True)
    porteiro = database.Column(database.String(20), nullable=False)
    
    data_retirada = database.Column(database.DateTime, nullable=True)
    retirado_por = database.Column(database.String(10), nullable=True)
    status = database.Column(database.String(20), default='Pendente')

    morador_id = database.Column(database.Integer, database.ForeignKey('morador.id'), nullable=False)
    morador = database.relationship('Morador', backref='encomendas')