from django import forms
from barberApp.models import Cita

tipo_corte = [
    ('corte', 'corte'),
    ('cejas', 'cejas'),
    ('barba', 'barba'),
    ('corte y cejas', 'corte y cejas'),
    ('corte y barba', 'corte y barba'),
    ('corte completo', 'corte completo'),
]


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha', 'hora', 'descripcion', 'tipo_corte')

    # fecha = forms.DateTimeField()
    # hora = forms.TimeField()
    # descripcion = forms.CharField()
    # tipo_corte = forms.ChoiceField(tipo_corte)
