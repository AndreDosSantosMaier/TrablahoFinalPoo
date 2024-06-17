from flask import request
from flask import render_template

def hubHtmlController():
        if request.method == 'GET':
            return render_template('Hub.html')