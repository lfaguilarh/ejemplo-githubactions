from utils.db import db

class Notas(db.Model):
    __tablename__ = 'notas'
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable = False)
    descripcion = db.Column(db.String(250), nullable = False)

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion