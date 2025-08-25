from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import ws_app.routing

websocket_urlpatterns = [
    *ws_app.routing.websocket_urlpatterns,
]
