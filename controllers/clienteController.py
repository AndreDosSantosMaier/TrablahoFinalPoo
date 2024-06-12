from flask import request
from database.db import db
from models.cliente import Clientes
from models.hotel import Hotel
from flask import render_template


def clienteController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            cliente = Clientes(data['cpf'], data['nome'], data['telefone'], data['codhotel'], data['codquarto'], data['codatividade'])
            db.session.add(cliente)
            db.session.commit()
            return 'Cliente criado com sucesso',200
        except Exception as e: 
            return 'O Cliente nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Clientes.query.all()
            cliente = {'clientes': [cliente.to_dict() for cliente in data]}
            return cliente,200
        except Exception as e:
            return 'O Quarto nao foi encontrado. Erro: {}'.format(str(e)),405