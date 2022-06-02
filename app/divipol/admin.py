from django.contrib import admin
from app.divipol.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DivipolAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['departamento','ciudad','nombre','referencia','comentario']
    search_fields =  ['departamento','ciudad','nombre','referencia']

admin.site.register(DivipolModel,DivipolAdmin)