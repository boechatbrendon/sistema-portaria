from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class Formlogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', validators=[DataRequired()], render_kw={'placeholder': 'Senha'})
    botao_login = SubmitField('Login')


class FormMorador(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()], render_kw={"placeholder": "Nome completo"})
    cpf = StringField('CPF', validators=[DataRequired()], render_kw={"placeholder": "Digite o CPF"})
    email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={"placeholder": "Digite o E-mail"})
    celular = StringField('Celular', validators=[DataRequired()], render_kw={"placeholder": "Digite o numero de celular"})
    unidade = SelectField('Unidade', choices=[], coerce=int)
    botao_cadastra = SubmitField('Cadastra')