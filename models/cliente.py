from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Clientes(db.Model):
    def to_dict(self):
        return{
            'cpf': self.cpf,
            'nome':self.nome,
            'telefone': self.telefone,
            'codhotel': self.codhotel,
            'codquarto': self.codquarto,
            'codatividade': self.codatividade
        }
    cpf =  db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(70))
    telefone =  db.Column(db.Integer)
    codhotel = db.Column(ForeignKey('hotel.codigo'))
    hotel = relationship('Hoteis', backref= 'cliente')
    codquarto = db.Column(ForeignKey('quarto.codigo'))
    quarto = relationship('Quartos', backref= 'cliente')
    codatividade = db.Column(ForeignKey('atividade.codigo'))
    atividade = relationship('Atividade', backref= 'cliente')
    def __init__(self,cpf, nome, telefone, codhotel, codquarto, codatividade):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.codhotel = codhotel
        self.codquarto = codquarto
        self.codatividade = codatividade