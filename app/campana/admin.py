from django.contrib import admin
from app.campana.models import *
from import_export.admin import ImportExportModelAdmin

class CampanaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['nombre','eslogan','logo','partido','candidato']
    search_fields =  ['nombre','eslogan','partido','candidato']

admin.site.register(CampanaModel,CampanaAdmin)