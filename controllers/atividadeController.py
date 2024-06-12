from flask import request
from database.db import db
from models.atividade import Atividades
from flask import render_template


def atividadesController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            quarto = Atividades(data['descricao'], data['preco'], data['horario'], data['local'], data['codhotel'])
            db.session.add(quarto)
            db.session.commit()
            return 'Quarto criado com sucesso',200
        except Exception as e: 
            return 'O quarto nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Atividades.query.all()
            print([atividade.to_dict() for atividade in data ])
            teste = {'atividades': [atividade.to_dict() for atividade in data]}
            return teste,200
        except Exception as e:
            return 'O Quarto nao foi encontrado. Erro: {}'.format(str(e)),405