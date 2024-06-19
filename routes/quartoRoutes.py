from controllers.QuartoController import quartosController
from controllers.quartoCadastro import quartoHtmlController
def quartoRoutes(app):
    app.route('/quarto', methods= ['GET', 'POST', 'DELETE'])(quartosController)
    app.route('/quartoHtml', methods= ['GET'])(quartoHtmlController)