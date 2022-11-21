from django import forms 
from barberApp.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= '__all__'