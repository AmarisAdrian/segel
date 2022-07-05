from django.db import models
from app.divipol.models import *
# Create your models here.

class ZonaVotacionModel(models.Model):
    id = models.AutoField(primary_key=True,db_column='id')
    divipol = models.ForeignKey(DivipolModel, on_delete=models.CASCADE, db_column='divipol')
    numero = models.IntegerField(unique=True,db_column='numero',blank=True, null=True)
    codigo = models.CharField(max_length=45,db_column='codigo', blank=True, null=True)
    nombre = models.CharField(max_length=20,db_column='nombre', blank=True, null=True)
    is_active=models.BooleanField(default=False)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.divipol

    class Meta:
        managed = True
        db_table = 'zona_votacion'
        verbose_name="zona votacion"
        verbose_name_plural= 'zona votaciones' 