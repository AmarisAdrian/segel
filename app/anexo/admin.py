from django.contrib import admin
from app.anexo.models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class AnexoUsuario(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['votante','imagen','comentario']
    search_fields =  ['votante','imagen','comentario']


admin.site.register(AnexoModel,AnexoUsuario)
