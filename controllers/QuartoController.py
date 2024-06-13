from flask import request
from database.db import db
from models.quarto import Quartos
from flask import render_template


def quartosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            quarto = Quartos(data['capacidade'], data['codhotel'], data['numero'])
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
        
    elif request.method == "DELETE":
        try:
            data = request.get_json()
            delete_quarto = data["codigo"]
            quarto = Quartos.query.get(delete_quarto)
            if quarto is None:
                return {'error':'Quarto nao encontrado'}, 404
            db.session.delete(quarto)
            db.session.commit()
            return 'Quarto deletado com sucesso',202
        except Exception as e:
            return 'Não foi possivel deletar o quarto'