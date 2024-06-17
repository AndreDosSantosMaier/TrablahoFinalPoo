from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Atividades(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'descricao': self.descricao,
            'preco': self.preco,
            'horario': self.horario,
            'local': self.local,

        }
    codigo =  db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.String(200))
    preco = db.Column(db.Float(5,2))
    horario = db.Column(db.String(5))
    local = db.Column(db.String(100))



    
    def __init__(self, descricao, preco, horario, local):
        self.descricao = descricao
        self.preco = preco
        self.horario = horario
        self.local = local