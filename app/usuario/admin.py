from django.contrib import admin
from app.usuario.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id','username','password','first_name','last_name','email','is_staff','is_active','is_superuser',
    'is_admin','is_lider','is_manager','tipo_documento','campana','nodocumento','firma','movil','fijo','direccion','departamento','ciudad','last_login','date_joined']
    search_fields =  ['nodocumento','campana','ciudad']

class VotanteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['tipo_documento','nodocumento','firma','movil','direccion','departamento','ciudad']
    search_fields =  ['nodocumento','ciudad']

class Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name','active','user_id',)
class ManagerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name','active','user_id',)
class LiderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','name','active','user_id',)  

admin.site.register(User,UsuarioAdmin)
admin.site.register(VotanteModel,VotanteAdmin)
admin.site.register(AdminProfile,Admin)
admin.site.register(LiderProfile,LiderAdmin)
admin.site.register(ManagerProfile,ManagerAdmin)