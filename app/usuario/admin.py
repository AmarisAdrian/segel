from django.contrib import admin
from app.usuario.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['tipo_documento','estado_usuario','campana','nodocumento','nombre','apellido','firma','movil','fijo','direccion','departamento','ciudad']
    search_fields =  ['nodocumento','estado_usuario','campana','ciudad']

admin.site.register(User,UsuarioAdmin)