from django.contrib import admin
from app.registro_votante.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class RegistroVotanteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['votante','puesto','mesa','comentario']
    search_fields =  ['votante','puesto','mesa']

admin.site.register(RegistroVotanteModel,RegistroVotanteAdmin)