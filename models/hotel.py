from database.db import db

class Hotel(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'gerente':self.gerente,
            'cidade': self.cidade,
            'telefone': self.telefone,
        }
    codigo =  db.Column(db.Integer, primary_key = True, unique = True, autoincrement=True )
    gerente = db.Column(db.String(70))
    cidade = db.Column(db.String(100))
    telefone =  db.Column(db.Integer)

    def __init__(self, gerente, cidade, telefone):
        self.gerente = gerente
        self.cidade = cidade
        self.telefone = telefone
