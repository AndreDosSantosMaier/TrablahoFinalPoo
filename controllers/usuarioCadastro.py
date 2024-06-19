from flask import request
from database.db import db
from models.usuario import Usuario
from flask import render_template

def usuarioHtmlController():
    if request.method == 'GET':
        return render_template('User.html')
