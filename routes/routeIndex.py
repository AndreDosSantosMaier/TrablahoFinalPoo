from routes.usuarioRoutes import usuarioRoutes
from routes.quartoRoutes import quartoRoutes
from routes.atividadesRoutes import atividadesRoutes
from routes.clientesRoutes import clientesRoutes
from routes.loginRoutes import loginRoutes
def routeIndex(app):
    usuarioRoutes(app=app)
    quartoRoutes(app=app)
    atividadesRoutes(app= app)
    clientesRoutes(app=app)
    loginRoutes(app=app)
