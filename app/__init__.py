from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '2caab23718c75c40096efa7832d60f6eec7f7d50fda2899df091df3afc08df4f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config["UPLOAD_FOLDER"] = "static/fotos_moradores"

database = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from app import routes