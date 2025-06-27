from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class Formlogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', validators=[DataRequired()], render_kw={'placeholder': 'Senha'})
    botao_login = SubmitField('Login')