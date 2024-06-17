from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Quartos(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'capacidade':self.capacidade,
            'numero': self.numero
        }
    codigo =  db.Column(db.Integer,primary_key=True)
    capacidade = db.Column(db.String(70))
    numero = db.Column(db.String(3))


    def __init__(self, capacidade, numero):
        self.capacidade = capacidade
        self.numero = numero
        
