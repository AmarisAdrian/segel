from django.contrib import admin
from app.puesto_votacion.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class PuestoVotacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['zona','codigo','nombre','direccion','mesa','potencial']
    search_fields =  ['zona','codigo','nombre','direccion','mesa','potencial']

admin.site.register(PuestoVotacionModel,PuestoVotacionAdmin)
