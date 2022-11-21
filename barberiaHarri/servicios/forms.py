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


class TimeInput(forms.TimeInput):
    input_type = "time"


class DateInput(forms.DateInput):
    input_type = "date"


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ('fecha', 'hora', 'descripcion', 'tipo_corte','usuario')
        widgets = {'fecha': DateInput(), 'hora': TimeInput(), }
