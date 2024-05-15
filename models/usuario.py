from database.db import db

class Usuario(db.Model):
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'email': self.email,
            'senha': self.senha
        }
    codigo = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    email = db.Column(db.String(70))
    senha = db.Column(db.Integer)

    def __init__(self,codigo,email, senha):
        self.codigo = codigo
        self.email = email
        self.senha = senha