from flask import request
from database.db import db
from models.atividade import Atividades
from flask import render_template

def atividadesHtmlController():
    if request.method == 'GET':
        return render_template('Atividades.html')
