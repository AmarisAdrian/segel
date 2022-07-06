from django.contrib import admin

from django.contrib import admin
from app.config.models import *
from import_export.admin import ImportExportModelAdmin

class DepartamentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','nombre','is_active']
    search_fields = ['nombre']

class CiudadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','nombre','is_active']
    search_fields = ['nombre']

class ConfiguracionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','manejador','valor']
    search_fields = ['manejador']

class LogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','modulo', 'request','excepcion','fecha_ingreso']
    search_fields = ['modulo']

class GeneroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

class TipoDocumentoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

admin.site.register(DepartamentoModel,DepartamentoAdmin)
admin.site.register(CiudadModel,CiudadAdmin)
admin.site.register(ConfiguracionModel,ConfiguracionAdmin)
admin.site.register(LogModel,LogAdmin)
admin.site.register(GeneroModel,GeneroAdmin)
admin.site.register(TipoDocumentoModel,TipoDocumentoAdmin)