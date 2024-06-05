from flask import request
from database.db import db
from models.usuario import Usuario
from flask import render_template


def usuarioController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = Usuario(data['email'], data['senha'], data['nome'])
            db.session.add(user)
            db.session.commit()
            return 'Usuario criado com sucesso',200
        except Exception as e: 
            return 'O usuario nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Usuario.query.all()
            print([user.to_dict() for user in data ])
            teste = {'users': [user.to_dict() for user in data]}
            return teste,200
        except Exception as e:
            return 'O usuario nao foi encontrado. Erro: {}'.format(str(e)),405