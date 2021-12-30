
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from estado.api.viewsets import EstadoViewSet
from municipio.api.viewsets import MunicipioViewSet
from pais.api.viewsets import PaisViewSet

router = routers.DefaultRouter()
router.register('estado', EstadoViewSet)
router.register('municipio', MunicipioViewSet)
router.register('pais', PaisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]