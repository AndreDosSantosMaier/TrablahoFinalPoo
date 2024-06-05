from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Usuario(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'email': self.email,
            'senha': self.senha,
            'nome': self.nome
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, autoincrement=True)
    email = db.Column(db.String(70))
    senha = db.Column(db.Integer)
    nome = db.Column(db.String(45))

    def __init__(self,email, senha, nome):
        self.email = email
        self.senha = senha
        self.nome = nome