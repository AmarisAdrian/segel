from django.shortcuts import render ,redirect
from django.views.generic import *
from app.usuario.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import *
from app.config.forms import *
from app.config.response import *
from app.config.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from app.config.response import *
from django.urls import reverse_lazy
from sweetify.views import SweetifySuccessMixin
import logging

# Create your views here.
@login_required
def Ciudad(request): 
    try:
        logger = logging.getLogger()
        login_url = '/perfil/login/'
        redirect_field_name = 'redirect_to'
        ciudad = CiudadModel.objects.all()
        form_class = CiudadForm
        departamento = DepartamentoModel.objects.all()
    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
    return render(request,'config/ciudad.html',locals())

@login_required
@require_http_methods(["POST"])
def CreateCiudad(request): 
    logger = logging.getLogger()
    modulo = "Config/AddCiudad"
    try:
        if request.method == "POST":
            ciudad = CiudadModel.objects.latest('id')
            departamento = request.POST.get('id_departamento')
            nombre = request.POST.get('id_nombre')
            if CiudadModel.objects.filter(nombre = nombre):
                response = Error("El nombre de la ciudad se encuentra registrado")
                RegistrarLog(modulo , "El nombre de la ciudad se encuentra registrado",request.POST)
            else:
                Ciudad = CiudadModel()
                departamento = DepartamentoModel.objects.get(id = departamento)
                id_ciudad = ciudad.id + 1
                Ciudad.id = id_ciudad
                Ciudad.departamento = departamento
                Ciudad.nombre = nombre
                Ciudad.save()
                sw = True
                if sw :
                    response = Success("Nombre de la ciudad registrado exitosamente")
                else:
                    response = Error("No se pudo registrar la ciudad")
                    RegistrarLog(modulo , "No se pudo registrar la ciudad",request.POST)
            return JsonResponse(response,safe=False)
    except Exception as ex:
        response = Error500('Informacion no procesada: ' + str(ex));
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
        return JsonResponse(response,safe=False)

@login_required
@require_http_methods(["GET"])
def GetCiudad(request,pk):
    model = CiudadModel
    logger = logging.getLogger()
    modulo = "Config/GetCiudad"
    form = CiudadForm
    try:
        if request.method == "GET":
            if pk != None or pk != "":
                ciudad = model.objects.filter(id=pk).exists()
                if ciudad:
                    ciudad = model.objects.get(id=pk)
                    ciudad = {
                        'id' : ciudad.id,
                        'departamento': ciudad.departamento,
                        'nombre' : ciudad.nombre,
                        'estado': ciudad.is_active,
                        'form': form
                    }          
                    response = GetResponse("Ciudad encontrada",ciudad)
                else:
                    response = Error("Ciudad no encontrada")
                    RegistrarLog(modulo , "Ciudad no encontrada",request.POST)
            else:
                response = Error500("Ha ocurrido un error de validacion")
                RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)
            return render(request, 'config/modal-ciudad.html', response)
    except Exception as ex:
        response = Error500('Informacion no procesada: ' + str(ex));
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
        RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)
        return JsonResponse(response,safe=False)


@login_required
@require_http_methods(["GET"])
def GetCiudadByDepartamento(request,pk):
    model = CiudadModel
    logger = logging.getLogger()
    modulo = "Config/GetCiudadByDepartamento"
    try:
        if request.method == "GET":
            if pk != None or pk != "":
                ciudad = model.objects.filter(departamento=pk).exists()
                if ciudad:
                    ciudad = model.objects.get(departamento=pk)
                else:
                    RegistrarLog(modulo , "Ciudad no encontrada",request.POST)
            else:
                RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)
            return render(request, locals())
    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
        RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)

class UpdateCiudad(LoginRequiredMixin,SweetifySuccessMixin,UpdateView):
    login_url = '/perfil/login/'
    redirect_field_name = 'redirect_to'
    model = CiudadModel
    success_url = reverse_lazy('config:ciudad')
    form_class = CiudadForm
    success_message = 'Ciudad actualizada exitosamente'
    def get_context_data(self, **kwargs):    
        context = super(UpdateCiudad, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        ciudad = self.model.objects.get(id=pk)       
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET) 
        return context
        
    def post(self, request, *args, **kwargs):
        modulo = "Config/UpdateCiudad/post"
        self.object = self.get_object
        id = kwargs['pk']
        ciudad = self.model.objects.get(id=id)
        form = self.form_class(self.request.POST,instance=ciudad)  
        success_message = 'Ciudad actualizada exitosamente'  
        try:
            if form.is_valid():
                sw = form.save(commit=False)
                sw.save()
                SuccessMessage(self.request,'La ciudad se ha actualizado exitosamente')        
            else:
                ErrorMessage(self.request,'ha ocurrido un error al actualizar la ciudad')
                RegistrarLog(modulo, 'Ha ocurrido un error'+ str(form.errors) ,self.request.POST) 
                return render(request, 'config/ciudad.html', {'form': form})
            return redirect('config:ciudad')
        except Exception as ex:
            RegistrarLog(modulo, 'Excepcion controlada: '+ str(ex) ,self.request.POST)
            ErrorMessage(self.request,ex)
            return redirect('config:ciudad')

@login_required
def Departamento(request): 
    try:
        logger = logging.getLogger()
        login_url = '/perfil/login/'
        redirect_field_name = 'redirect_to'
        form_class = DepartamentoForm
        departamento = DepartamentoModel.objects.all()
    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
    return render(request,'config/departamento.html',locals())

            

@login_required
@require_http_methods(["POST"])
def CreateDepartamento(request):
        logger = logging.getLogger()
        modulo = "Config/CreateDepartamento/post"
        try:
            if  request.method == "POST":
                departamento = DepartamentoModel() 
                sw = DepartamentoModel.objects.latest('id')
                departamento.id = sw.id + 1
                departamento.nombre = request.POST.get('nombre')
                departamento.save()
                SuccessMessage(request,'El departamento se ha registrado correctamente')                    
            else:
                ErrorMessage(request,'Ha ocurrido un error')
                RegistrarLog(modulo, 'No se pudo guardar el departamento',request.POST) 
            return redirect('config:departamento') 
        except Exception as ex:
            RegistrarLog(modulo, 'Excepcion controlada: '+ str(ex) ,request.POST)
            ErrorMessage(request,ex)
            return redirect('config:departamento')



class UpdateDepartamento(LoginRequiredMixin,SweetifySuccessMixin,UpdateView):
    login_url = '/perfil/login/'
    redirect_field_name = 'redirect_to'
    model = DepartamentoModel
    success_url = reverse_lazy('config:departamento')
    form_class = DepartamentoForm
    success_message = 'Departamento actualizado exitosamente'
    def get_context_data(self, **kwargs):    
        context = super(UpdateDepartamento, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        departamento = self.model.objects.get(id=pk)       
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET) 
        return context
        
    def post(self, request, *args, **kwargs):
        modulo = "Config/UpdateDepartamento/post"
        self.object = self.get_object
        id = kwargs['pk']
        departamento = self.model.objects.get(id=id)
        form = self.form_class(self.request.POST,instance=departamento)  
        success_message = 'Departamento actualizado exitosamente'  
        try:
            if form.is_valid():
                sw = form.save(commit=False)
                sw.save()
                SuccessMessage(self.request,'El departamento se ha actualizado exitosamente')        
            else:
                ErrorMessage(self.request,'ha ocurrido un error al actualizar el departamento')
                RegistrarLog(modulo, 'Ha ocurrido un error'+ str(form.errors) ,self.request.POST) 
                return render(request, 'config/departamento.html', {'form': form})
            return redirect('config:departamento')
        except Exception as ex:
            RegistrarLog(modulo, 'Excepcion controlada: '+ str(ex) ,self.request.POST)
            ErrorMessage(self.request,ex)
            return redirect('config:departamento')


@login_required
@require_http_methods(["GET"])
def GetDepartamento(request,pk):
    model = DepartamentoModel
    logger = logging.getLogger()
    modulo = "Config/GetDepartamento"
    form = DepartamentoForm
    try:
        if request.method == "GET":
            if pk != None or pk != "":
                departamento = model.objects.filter(id=pk).exists()
                if departamento:
                    departamento = model.objects.get(id=pk)
                    departamento = {
                        'id' : departamento.id,
                        'nombre' : departamento.nombre,
                        'estado': departamento.is_active,
                        'form': form
                    }          
                    response = GetResponse("Departamento encontrado",departamento)
                else:
                    response = Error("Departamento no encontrado")
                    RegistrarLog(modulo , "Departamento no encontrado",request.POST)
            else:
                response = Error500("Ha ocurrido un error de validacion")
                RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)
            return render(request, 'config/modal-departamento.html', response)
    except Exception as ex:
        response = Error500('Informacion no procesada: ' + str(ex));
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
        RegistrarLog(modulo , "Ha ocurrido un error de validacion",request.POST)
        return JsonResponse(response,safe=False)

@login_required
def Log(request): 
    try:
        logger = logging.getLogger()
        login_url = '/perfil/login/'
        redirect_field_name = 'redirect_to'
        log = LogModel.objects.all()
    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
    return render(request,'config/log.html',locals())

def RegistrarLog(modulo , Excepcion,*requested):
    model = LogModel
    logger = logging.getLogger()
    try:
        if modulo != '' and Excepcion != '' and requested != '':
            log = LogModel()
            log.modulo = modulo
            log.excepcion = Excepcion
            log.request = requested
            log.save()
        else: 
            logger.exception('Excepcion controlada: ' + str(ex))
            logger.error('Excepcion controlada: ' + str(ex))
    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))