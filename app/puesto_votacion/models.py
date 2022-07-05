from django.db import models
from app.zona_votacion import *
from app.zona_votacion.models import ZonaVotacionModel
# Create your models here.
class PuestoVotacionModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    zona = models.ForeignKey(ZonaVotacionModel,  on_delete=models.CASCADE, db_column='zona')
    codigo = models.CharField(max_length=150,unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=150, blank=False, null=False)
    direccion = models.CharField(max_length=60, blank=False, null=False)
    mesa = models.IntegerField()
    potencial = models.IntegerField()
    is_active=models.BooleanField(default=False)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.zona
        
    class Meta:
        managed = True
        db_table = 'puesto_votacion'
        verbose_name="puesto votacion"
        verbose_name_plural= 'puesto de votaciones' 