from routes.usuarioRoutes import usuarioRoutes
from routes.hotelRoutes import hotelRoutes
def routeIndex(app):
    usuarioRoutes(app=app)
    hotelRoutes(app=app)
