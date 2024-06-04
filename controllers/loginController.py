from flask import request
from database.db import db
from models.usuario import Usuario
from flask import render_template
    
def loginController():
    #render_template('login.html')
    if request.method == 'GET': 
        try:
            data = Usuario.query.all()
            print([usuario.to_dict() for usuario in data ])
            teste = {'usuario': [usuario.to_dict() for usuario in data]}
            return teste,200
        except Exception as e:
            return 'O usuario nao foi encontrado. Erro: {}'.format(str(e)),405
    
