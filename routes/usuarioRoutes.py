from controllers.usuarioController import usuarioController
from controllers.usuarioCadastro import usuarioHtmlController

def usuarioRoutes(app):
    app.route('/user', methods= ['GET', 'POST', 'DELETE'])(usuarioController)
    app.route('/userHtml', methods= ['GET'])(usuarioHtmlController)