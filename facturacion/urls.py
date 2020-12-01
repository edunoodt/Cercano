from django.urls import path
from . import views

urlpatterns = [
    path('', views.facturalia),
    path('contactos/',views.consulta_contacto),
    path('productos/',views.consulta_producto),
    path('empresas/',views.consulta_empresa),

]