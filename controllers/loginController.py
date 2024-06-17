from flask import request
from database.db import db
from models.usuario import Usuario
from flask import render_template


def loginController():
    if request.method == 'GET': 
        try:
            data = Usuario.query.all()
            print([usuario.to_dict() for usuario in data ])
            user = {'usuarios': [usuario.to_dict() for usuario in data]}
            return user,200
        except Exception as e:
            return 'Usuarios nao foram encontrados. Erro: {}'.format(str(e)),405