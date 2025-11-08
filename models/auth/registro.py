from utils.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Registro(db.Model):
    __tablename__ = 'registro'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100),unique=True, nullable=False)
    correo = db.Column(db.String(100),unique=True, nullable=False)
    contrasena = db.Column(db.String(100))
    
    def __init__(self,usuario, correo, contrasena):
        self.usuario = usuario
        self.correo = correo
        self.contrasena = self.encrypt_password(contrasena)
    
    def check_password(self,encrypt_contrasena,contrasena):
        return check_password_hash(encrypt_contrasena,contrasena)
    
    def encrypt_password(self, contrasena):
        return generate_password_hash(contrasena, 10)
    

    
