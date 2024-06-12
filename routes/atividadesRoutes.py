from controllers.atividadeController import atividadesController
from controllers.atividadeCadasro import atividadesHtmlController
def atividadesRoutes(app):
    app.route('/atividades', methods= ['GET', 'POST'])(atividadesController)
    app.route('/atividadesHtml', methods= ['GET','POST'])(atividadesHtmlController)