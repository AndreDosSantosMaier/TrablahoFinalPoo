from controllers.hotelCadastro import hotelHtmlController
from controllers.hotelController import hotelController
def hotelRoutes(app):
    app.route('/hotel', methods= ['GET', 'POST', 'DELETE'])(hotelController)
    app.route('/hotelHtml', methods= ['GET'])(hotelHtmlController)