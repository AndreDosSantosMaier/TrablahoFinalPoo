from flask import request
from database.db import db
from models.quarto import Quartos
from flask import render_template

def quartoHtmlController():
    if request.method == 'GET':
        return render_template('Quarto.html')
