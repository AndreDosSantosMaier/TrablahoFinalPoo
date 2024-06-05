from flask import request
from database.db import db
from models.hotel import Hotel
from flask import render_template

def hotelHtmlController():
    if request.method == 'GET':
        return render_template('Hotel.html')
