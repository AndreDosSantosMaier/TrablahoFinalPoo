from routes.usuarioRoutes import usuarioRoutes
from routes.hotelRoutes import hotelRoutes
from routes.quartoRoutes import quartoRoutes
from routes.atividadesRoutes import atividadesRoutes
from routes.clientesRoutes import clientesRoutes
def routeIndex(app):
    usuarioRoutes(app=app)
    hotelRoutes(app=app)
    quartoRoutes(app=app)
    atividadesRoutes(app= app)
    clientesRoutes(app=app)
