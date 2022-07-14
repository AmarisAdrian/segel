from django.db import models

class DepartamentoModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=150,db_column='nombre',blank=False, null=False)
    is_active=models.BooleanField(default=True,blank=True, null=True)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.nombre

    def get_estado(self):
        if self.is_active:
            return "Activo"
        else:
            return "Inactivo"
    class Meta:
        managed = True
        db_table = 'departamento'
        verbose_name="Departamento"
        verbose_name_plural= 'Departamentos' 

class CiudadModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=150,db_column='nombre',blank=False, null=False)
    departamento = models.ForeignKey(DepartamentoModel, models.DO_NOTHING, db_column='departamento')
    is_active=models.BooleanField(default=True)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.departamento

    def __str__(self):
        return self.nombre
   
    def get_estado(self):
        if self.is_active:
            return "Activo"
        else:
            return "Inactivo"

    class Meta:
        managed = True
        db_table = 'ciudad'
        verbose_name="ciudad"
        verbose_name_plural= 'ciudades' 

class ConfiguracionModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=255,db_column='nombre',blank=False, null=False)
    manejador = models.CharField(max_length=50,db_column='manejador',blank=False, null=False)
    valor = models.CharField(max_length=255,db_column='valor',blank=False, null=False)
    is_active=models.BooleanField(default=False)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'configuracion'
        verbose_name="configuracion"
        verbose_name_plural= 'configuraciones' 


class LogModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    modulo = models.CharField(db_column='modulo', max_length=300)
    request = models.CharField(db_column='request', max_length=800, null= True,blank=True)
    excepcion = models.CharField(db_column='excepcion', max_length=600)
    fecha_ingreso = models.DateTimeField(db_column='fecha_ingreso', auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'log'
        verbose_name="log"
        verbose_name_plural= 'logs' 

class GeneroModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=15, blank=False, null=False)
    is_active=models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'genero'
        verbose_name="genero"
        verbose_name_plural= 'generos' 

class TipoDocumentoModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    is_active=models.BooleanField(default=False)
    class Meta:
        managed = True
        db_table = 'tipo_documento'
        verbose_name="Tipo de documentos"
        verbose_name_plural= 'Tipo documentos' 
