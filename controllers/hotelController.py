from flask import request
from database.db import db
from models.hotel import Hotel
from flask import render_template


def hotelController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            hotel = Hotel(data['gerente'], data['cidade'], data['telefone'])
            db.session.add(hotel)
            db.session.commit()
            return 'Hotel criado com sucesso',200
        except Exception as e: 
            return 'O Hotel nao foi criado. Erro: {}'.format(str(e)),405
    elif request.method == 'GET': 
        try:
            data = Hotel.query.all()
            print([hotel.to_dict() for hotel in data ])
            teste = {'hotels': [hotel.to_dict() for hotel in data]}
            return teste,200
        except Exception as e:
            return 'O usuario nao foi encontrado. Erro: {}'.format(str(e)),405