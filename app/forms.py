from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Morador
from flask_wtf.file import FileField, FileAllowed

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
    foto = FileField('Foto Perfil', validators=[FileAllowed(['jpg', 'png'])])
    botao_cadastra = SubmitField('Cadastra')

    def validate_email(self, email):
        morador = Morador.query.filter_by(email=email.data).first()
        if morador:
            raise ValidationError('Ja existe um Morador cadastrado com esse email, Porfavor adicione outro E-mail')
        
    def validate_cpf(self, cpf):
        cpf_limpo = ''.join(filter(str.isdigit, cpf.data))
        morador = Morador.query.filter_by(cpf=cpf_limpo).first()
        if morador:
            raise ValidationError('Morador com o CPF informado Ja esta Cadastrado')
        
    
class FormEncomenda(FlaskForm):
    unidade = SelectField('Unidade', choices=[], coerce=int)
    nf = StringField('Nota Fiscal', validators=[DataRequired()])
    botao_cadastra =SubmitField('Cadastra Encomenda')


class FormHistoricoEncomenda(FlaskForm):
    data_inicial = DateField('Data inicial',format='%Y-%m-%d' ,validators=[DataRequired()])
    data_final = DateField('Data Final',format='%Y-%m-%d' ,validators=[DataRequired()])
    botao_busca = SubmitField('Buscar')