from django.shortcuts import render
from barberApp.models import Servicio

# Create your views here.


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def cita(request):
    return render(request, 'cita.html')


def edicion(request):
    return render(request, 'edicion.html')


def evento(request):
    return render(request, 'evento.html')


def perforacion(request):
    return render(request, 'perforacion.html')


def publicidad(request):
    return render(request, 'publicidad.html')
