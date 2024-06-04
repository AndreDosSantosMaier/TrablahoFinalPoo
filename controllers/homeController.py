from models.cliente import Clientes
from flask import render_template
def homeController():
    return render_template("home.html", user=user)