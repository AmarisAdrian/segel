from django.db import models


class CampanaModel(models.Model):
    nombre = models.CharField(max_length=255, db_column='nombre',blank=True, null=True)
    eslogan = models.CharField(max_length=255, db_column='eslogan',blank=True, null=True)
    logo = models.FileField(upload_to='soporte/', db_column='logo',blank=True, null=True)
    partido = models.CharField(max_length=255, db_column='partido',blank=True, null=True)
    candidato = models.CharField(max_length=255, db_column='candidato',blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'campana'
        verbose_name="Campaña"
        verbose_name_plural= 'Campaña' 
        