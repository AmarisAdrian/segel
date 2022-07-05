from django.db import models
from app.usuario.models import *

# Create your models here.
class AnexoModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    votante = models.ForeignKey(VotanteModel ,on_delete=models.CASCADE,blank=True, null=True)
    imagen = models.FileField(upload_to='soporte/',blank=False, null=False)
    comentario = models.CharField(max_length=100, blank=False, null=True)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.votante

    class Meta:
        managed = True
        db_table = 'anexo'
        verbose_name="Anexo anexo"
        verbose_name_plural= 'Anexo usuarios' 
        
