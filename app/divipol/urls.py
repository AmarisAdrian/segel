from django.urls import path,include
from app.divipol.views import *

app_name = 'app.divipol'
urlpatterns = [
    path('',Divipol.as_view() ,name="divipol"),
]