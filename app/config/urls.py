from django.urls import path,include
from app.config.views import *

app_name = 'app.config'
urlpatterns = [
    path('ciudad',ciudad ,name="ciudad"),
    path('crear-ciudad',AddCiudad,name="crear-ciudad"),
    path('editar-ciudad/<int:pk>/',UpdateCiudad.as_view(),name="editar-ciudad"),
    path('consultar-ciudad/<int:pk>/', GetCiudad,name="consultar-ciudad"),
]