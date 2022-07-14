from django.shortcuts import render
from app.divipol.forms import DivipolForm
from app.divipol.models import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Divipol(LoginRequiredMixin,ListView): 
    login_url = '/perfil/login/'
    redirect_field_name = 'redirect_to'
    model = DivipolModel
    template_name = 'divipol/divipol.html'
    context_object_name = 'divipol'
    def get(self, request, *args, **kwargs):
        form_class = DivipolForm
        departamento = DepartamentoModel.objects.all()
        ciudad = CiudadModel.objects.all()
        return render(request,self.template_name,locals())

