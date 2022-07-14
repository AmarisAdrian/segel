from django import forms    
from app.divipol.models import *

class DivipolForm(forms.ModelForm):
    class Meta:
        model = DivipolModel
        fields = [
                'departamento',
                'ciudad',
                'nombre', 
                'referencia',
                'comentario',    
                'is_active'     
        ]
        labels = {
                'departamento':'* Departamento', 
                'ciudad':'* Ciudad', 
                'nombre':'* Nombre',  
                'referencia':'* Nombre',
                'comentario':' Comentario',      
                'is_active':'Activo'    
        }
        widgets = {
                'departamento': forms.Select(attrs={'class': 'form-control border border-2'}), 
                'ciudad': forms.Select(attrs={'class': 'form-control border border-2'}),    
                'nombre':forms.TextInput(attrs={'class': 'form-control border border-2'}),
                'referencia':forms.TextInput(attrs={'class': 'form-control border border-2'}),
                'comentario':forms.Textarea(attrs={'class': 'form-control border border-2', 'rows':'5', 'cols':'10' }),
                'is_active': forms.CheckboxInput(attrs={})
        }