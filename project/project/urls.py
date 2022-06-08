
from django.urls import path, include
from rest_framework import routers
from app.views import * 

router = routers.DefaultRouter()
# router.register('descargas', DescargasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('api/descargas/', lista_descargas),
    path('api/descargas/', lista_descargas_ultima_hora),

    path('api/descarga/<id>', detalhes_descarga),

    path('api/alvos', lista_alvos),
    path('api/alvo/<id>', detalhes_alvo),


]