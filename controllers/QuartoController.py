from flask import request
from database.db import db
from models.quarto import Quartos
from flask import render_template


def quartosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            quarto = Quartos(data['capacidade'], data['disponibilidade'], data['codhotel'], data['numero'])
            db.session.add(quarto)
            db.session.commit()
            return 'Quarto criado com sucesso',200
        except Exception as e: 
            return 'O quarto nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Quartos.query.all()
            print([quarto.to_dict() for quarto in data ])
            teste = {'quartos': [quarto.to_dict() for quarto in data]}
            return teste,200
        except Exception as e:
            return 'O Quarto nao foi encontrado. Erro: {}'.format(str(e)),405