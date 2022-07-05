from django.http import HttpResponseRedirect,  JsonResponse
import sweetify

def Success(Msj, datos = []):
    return  { 'status': 'success', 'code': 201, 'msj': Msj , 'datos': datos}

def Error(Msj, datos = []):
    return  { 'status': 'error', 'code': 200, 'msj': Msj , 'datos': datos}

def Error500(Msj, datos = []):
    return  { 'status': 'error', 'code': 500, 'msj': Msj , 'datos': datos}

def GetResponse(Msj, datos = {}):
    return  { 'status': 'success', 'code': 200, 'msj': Msj , 'datos': datos}

def SuccessMessage(request,Message):
    sweetify.success(request,'Proceso exitoso',text=Message,button='Ok',icon="success",timer=5000)

def ErrorMessage(request,Message):
    sweetify.error(request,'Proceso fallido', text=Message,button='Ok' ,icon="error",timer=10000)

def WarningMessage(request,Message):
    sweetify.warning(request,'¿Está seguro?', text=Message,button='Ok',icon="question", denyButtonText='Cancelar')

def InfoMessage(request,Message):
    sweetify.info(request,'Info', text=Message,button='Ok', denyButtonText='info')
