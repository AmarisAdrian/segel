from django.db import models
from app.config.models import *
from app.campana.models import *
from app.usuario.models import *
# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    id = models.AutoField(primary_key = True)
    tipo_documento = models.ForeignKey(TipoDocumentoModel, models.DO_NOTHING, db_column='tipo_documento',blank=True, null=True)
    campana = models.ForeignKey(CampanaModel, models.DO_NOTHING, db_column='campana' ,blank=True, null=True)
    nodocumento = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, db_column='nombre')
    apellido = models.CharField(max_length=45, db_column='apellido')
    genero = models.ForeignKey(GeneroModel, models.DO_NOTHING, db_column='genero',blank=True, null=True)
    movil = models.IntegerField(blank=True, null=True, db_column='movil')
    fijo = models.IntegerField(blank=True, null=True, db_column='fijo')
    direccion = models.CharField(max_length=70, db_column='direccion')
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento',blank=True, null=True)
    ciudad = models.ForeignKey(CiudadModel, models.DO_NOTHING, db_column='ciudad',blank=True, null=True)
    firma = models.FileField(upload_to='soporte/',blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_lider=models.BooleanField(default=False)

    def __str__(self):
        return self.tipo_documento
    def __str__(self):
        return self.campana
    def __str__(self):
        return self.genero
    def __str__(self):
        return self.departamento
    def __str__(self):
        return self.ciudad
    
    abstract = True

    def get_admin_profile(self):
        admin_profile = None
        if hasattr(self, 'adminprofile'):
            admin_profile = self.AdminProfile
        return admin_profile

    def get_manager_profile(self):
        Manager_profile = None
        if hasattr(self, 'managerprofile'):
            Manager_profile = self.ManagerProfile
        return Manager_profile
    
    def get_lider_profile(self):
        Lider_profile = None
        if hasattr(self, 'liderprofile'):
            Lider_profile = self.LiderProfile
        return Lider_profile

    class Meta:
        db_table = 'auth_user'

class LiderProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)

class ManagerProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)

class AdminProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class VotanteModel(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='usuario' ,blank=True, null=True)
    tipo_documento = models.ForeignKey(TipoDocumentoModel, models.DO_NOTHING, db_column='tipo_documento',blank=True, null=True)
    nodocumento = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, db_column='nombre')
    apellido = models.CharField(max_length=45, db_column='apellido')
    genero = models.ForeignKey(GeneroModel, models.DO_NOTHING, db_column='genero',blank=True, null=True)
    movil = models.IntegerField(blank=True, null=True, db_column='movil')
    direccion = models.CharField(max_length=70, db_column='direccion')
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento',blank=True, null=True)
    ciudad = models.ForeignKey(CiudadModel, models.DO_NOTHING, db_column='ciudad',blank=True, null=True)
    firma = models.FileField(upload_to='soporte/',blank=True, null=True)

    def __str__(self):
        return self.departamento 
    def __str__(self):
        return self.ciudad

    class Meta:
        managed = True
        db_table = 'votante'
        verbose_name="votante"
        verbose_name_plural= 'votante' 