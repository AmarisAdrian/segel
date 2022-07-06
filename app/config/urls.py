from django.urls import path,include
from app.config.views import *

app_name = 'app.config'
urlpatterns = [
    path('ciudad',Ciudad ,name="ciudad"),
    path('crear-ciudad',CreateCiudad,name="crear-ciudad"),
    path('editar-ciudad/<int:pk>/',UpdateCiudad.as_view(),name="editar-ciudad"),
    path('consultar-ciudad/<int:pk>/', GetCiudad,name="consultar-ciudad"),
    path('departamento',Departamento ,name="departamento"),
    path('crear-departamento',CreateDepartamento,name="crear-departamento"),
    path('editar-departamento/<int:pk>/',UpdateDepartamento.as_view(),name="editar-departamento"),
    path('consultar-departamento/<int:pk>/', GetDepartamento,name="consultar-departamento"),
    path('log',Log ,name="log"),
]