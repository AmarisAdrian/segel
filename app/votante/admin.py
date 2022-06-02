from django.contrib import admin
from app.votante.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class VotanteAdmmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['tipo_documento','estado_usuario','usuario','campana','nodocumento','nombre','apellido','firma','movil','fijo','direccion','departamento','ciudad']
    search_fields =  ['nodocumento','estado_usuario','usuario','campana','ciudad']

admin.site.register(VotanteModel,VotanteAdmmin)