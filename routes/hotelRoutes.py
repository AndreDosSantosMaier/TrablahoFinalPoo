from controllers.hotelCadastro import hotelHtmlController
from controllers.hotelController import hotelController
def hotelRoutes(app):
    app.route('/hotel', methods= ['GET', 'POST'])(hotelController)
    app.route('/hotelHtml', methods= ['GET','POST'])(hotelHtmlController)