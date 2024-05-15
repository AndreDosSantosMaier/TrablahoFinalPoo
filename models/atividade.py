from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Atividades(db.Model):
    def to_dict(self):
        return{
            'codigo': self.cpf,
            'descricao':self.nome,
            'preco': self.telefone,
            'horario': self.codhotel,
            'local': self.codquarto,
            'imagem': self.codatividade,
            'codhotel': self.codhotel
        }
    codigo =  db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.String(200))
    preco = db.Column(db.Float(5,2))
    horario = db.Column(db.DateTime)
    local = db.Column(db.String(100))
    imagem = db.Column(db.String(200))
    codhotel = db.Column(ForeignKey('hotel.codigo'))
    hotel = relationship('Hotel', backref= 'atividade')
    def __init__(self,codigo, descricao, preco, horario, local, imagem, codhotel, hotel):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.horario = horario
        self.local = local
        self.imagem = imagem
        self.codhotel = codhotel
        self.hotel = hotel