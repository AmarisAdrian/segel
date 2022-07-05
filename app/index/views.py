from django.shortcuts import render
from app.usuario.models import *
from app.anexo.models import *
from app.puesto_votacion.models import *
from app.config.views import *
from django.http import JsonResponse
import logging
from django.contrib.auth.decorators import login_required
from django.db import connection

@login_required
def index(request):
    logger = logging.getLogger()
    modulo = "index/index"
    try:
        campana = request.session.get('username')

        votante_count = VotanteModel.objects.count()
        lider_count = User.objects.filter(is_lider = True).count()
        puesto_count = PuestoVotacionModel.objects.count()
        anexo_count = AnexoModel.objects.count()

    except Exception as ex:
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
    return render(request,'layout/index.html',locals())

@login_required
def GetRankingCliente(id_campana):
    try:
        modulo = "index/GetRanking"
        logger = logging.getLogger()
        with connection.cursor() as cursor:         
            cursor.execute("""select  user.nodocumento,user.nombre,user.apellido,count(*) as cantidad 
                            from user,votante
                            where votante.usuario = user.id and user.campana = %
                            group  by noDocumento 
                            order by cantidad desc;""",(id_campana)) 
            data = cursor.fetchall()
            return data
    except Exception as ex:
        responseData = {
            'status': 'error',
            'code': 500,
            'msj': 'Informacion no procesada: ' + str(ex)
        }
        RegistrarLog(modulo,str(ex),'NULL')
        logger.exception('Excepcion controlada: ' + str(ex))
        logger.error('Excepcion controlada: ' + str(ex))
    return JsonResponse(responseData,safe=False)