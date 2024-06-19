from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Clientes(db.Model):
    def to_dict(self):
        return{
            'cpf': self.cpf,
            'nome':self.nome,
            'telefone': self.telefone,
            'codquarto': self.codquarto,
            'codatividade': self.codatividade
        }
    cpf =  db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(70))
    telefone =  db.Column(db.Integer)

    codquarto = db.Column(ForeignKey('quartos.codigo'))
    quarto = relationship('Quartos', backref= 'clientes')
    codatividade = db.Column(ForeignKey('atividades.codigo'))
    atividade = relationship('Atividades', backref= 'clientes')
    
    def __init__(self,cpf, nome, telefone, codquarto, codatividade):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.codquarto = codquarto
        self.codatividade = codatividade