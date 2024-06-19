from flask import request
from database.db import db
from models.cliente import Clientes
from flask import render_template

def clienteHtmlController():
    if request.method == 'GET':
        return render_template('Clientes.html')
