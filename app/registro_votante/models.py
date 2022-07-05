from django.db import models
from app.puesto_votacion.models import *
from app.usuario.models import *

class RegistroVotanteModel(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, db_column='usuario',unique=True, blank=True, null=True)
    puesto = models.ForeignKey(PuestoVotacionModel,  on_delete=models.CASCADE, db_column='puesto')
    mesa = models.IntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=100, blank=True, null=True)
    is_active=models.BooleanField(default=False)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.usuario
        
    class Meta:
        managed = True
        db_table = 'registro_votante'
        verbose_name="registro votante"
        verbose_name_plural= 'registro votantes' 