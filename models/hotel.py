from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Hoteis(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'gerente':self.gerente,
            'endereco': self.endereco,
            'telefone': self.telefone,
        }
    codigo =  db.Column(db.Integer,primary_key=True)
    gerente = db.Column(db.String(70))
    endereco = db.Column(db.String(100))
    telefone =  db.Column(db.Integer)

    def __init__(self,codigo, gerente, telefone, endereco):
        self.codigo = codigo
        self.gerente = gerente
        self.endereco = endereco
        self.telefone = telefone
