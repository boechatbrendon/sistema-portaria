from app import app, database
from app.models import Unidade, Encomenda, Morador, Usuario
with app.app_context():
    database.create_all()
    usuario = Usuario(nome='usuario_test', usuario='Admin', senha='admin')
    database.session.add(usuario)
    database.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)