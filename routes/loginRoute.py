from controllers.loginController import loginController
def loginRoutes(app):
        app.route('/login', methods = ['GET'])(loginController)