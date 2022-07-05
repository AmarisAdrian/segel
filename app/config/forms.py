from django import forms    
from app.config.models import *

class CiudadForm(forms.ModelForm):
        class Meta:
                model = CiudadModel
                fields = [
                        'departamento',
                        'nombre',    
                        'is_active'     
                ]
                labels = {
                        'departamento':'* Departamento', 
                        'nombre':'* Nombre',       
                        'is_active':'Activo'    
                }
                widgets = {
                        'departamento': forms.Select(attrs={'class': 'form-control border border-2'}),     
                        'nombre':forms.TextInput(attrs={'class': 'form-control border border-2'}),
                        'is_active': forms.CheckboxInput(attrs={})
                }