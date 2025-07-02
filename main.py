from app import app, database
from app.models import Unidade, Encomenda, Morador, Usuario

with app.app_context():
    us = Usuario(nome='usuario_test', usuario='Admin', senha='admin')
    database.session.add(us)
    database.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)