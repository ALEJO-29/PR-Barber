from django.shortcuts import render, HttpResponse
from barberApp.models import Servicio
from .forms import CitaForm

# Create your views here.


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def cita(request):
    form= CitaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse('Reservado con exito')
    return render(request, 'cita.html', {'form': form})


def edicion(request):
    return render(request, 'edicion.html')


def evento(request):
    return render(request, 'evento.html')


def perforacion(request):
    return render(request, 'perforacion.html')


def publicidad(request):
    return render(request, 'publicidad.html')


def producto(request):
    return render(request, 'productos.html')
