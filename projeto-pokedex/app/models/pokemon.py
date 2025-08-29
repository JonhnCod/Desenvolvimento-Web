from .. import database as db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    tipo = db.Column(db.String(120), nullable=False)
    cor = db.Column(db.String(100), nullable=True)
    habilidades = db.Column(db.String(200), nullable=True)
    habitat = db.Column(db.String(150), nullable=True)
    held_items = db.Column(db.String(200), nullable=True)
    onde_encontrar = db.Column(db.String(200), nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    evolucao = db.Column(db.String(200), nullable=True)
    fotos = db.Column(db.String(200), nullable=True)
    tamanho = db.Column(db.Float(200), nullable=True)
    peso = db.Column(db.Float(200), nullable=True)
