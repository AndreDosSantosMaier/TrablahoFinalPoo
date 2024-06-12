from controllers.clienteController import clienteController
from controllers.clienteCadastro import clienteHtmlController
def clientesRoutes(app):
    app.route('/clientes', methods= ['GET', 'POST'])(clienteController)
    app.route('/clientesHtml', methods= ['GET','POST'])(clienteHtmlController)