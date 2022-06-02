from django.contrib import admin
from app.anexo.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AnexoUsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['usuario','imagen','comentario']
    search_fields =  ['usuario','imagen','comentario']

class AnexoVotanteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['votante','imagen','comentario']
    search_fields =  ['votante','imagen','comentario']

admin.site.register(AnexoUsuarioModel,AnexoUsuarioAdmin)
admin.site.register(AnexoVotanteModel,AnexoVotanteAdmin)