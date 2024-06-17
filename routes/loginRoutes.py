from controllers.loginController import loginController
from controllers.login import loginHtmlController
from controllers.hub import hubHtmlController
def loginRoutes(app):
    app.route('/login', methods= ['GET'])(loginController)
    app.route('/', methods= ['GET'])(loginHtmlController)
    app.route('/hub', methods= ['GET'])(hubHtmlController)