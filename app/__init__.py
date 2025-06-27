from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = '2caab23718c75c40096efa7832d60f6eec7f7d50fda2899df091df3afc08df4f'


from app import routes