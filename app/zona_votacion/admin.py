from django.contrib import admin
from app.zona_votacion.models import *
from import_export.admin import ImportExportModelAdmin

class ZonaVotacionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','divipol','numero', 'codigo', 'nombre']
    search_fields = ['divipol','numero','codigo','ModelAdmin']

admin.site.register(ZonaVotacionModel,ZonaVotacionAdmin)