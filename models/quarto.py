from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Quartos(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'capacidade':self.capacidade,
            'disponibilidade': self.disponibilidade,
            'codhotel': self.codhotel,
            'numero': self.numero
        }
    codigo =  db.Column(db.Integer,primary_key=True)
    capacidade = db.Column(db.String(70))
    disponibilidade = db.Column(db.String(100))
    numero = db.Column(db.String(3))
    codhotel = db.Column(ForeignKey('hotel.codigo'))
    hotel = relationship('Hotel', backref= 'quarto')


    def __init__(self, capacidade, disponibilidade, codhotel, numero):
        self.capacidade = capacidade
        self.disponibilidade = disponibilidade
        self.codhotel = codhotel
        self.numero = numero
        
