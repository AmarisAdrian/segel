from django.db import models
from app.config.models import *

# Create your models here.
class DivipolModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento')
    ciudad = models.ForeignKey(CiudadModel, models.DO_NOTHING, db_column='ciudad')
    nombre = models.CharField(max_length=45)
    referencia = models.CharField(unique=True, max_length=60, blank=True, null=True)
    comentario = models.CharField(max_length=60, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.departamento 
    def __str__(self):
        return self.ciudad

    class Meta:
        managed = True
        db_table = 'divipol'
        verbose_name="Divipol"
        verbose_name_plural= 'Divipol' 