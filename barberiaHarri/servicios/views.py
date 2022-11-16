from django.shortcuts import render
from barberApp.models import Servicio
from barberApp.models import Producto
from .forms import CitaForm

# Create your views here.


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})


def cita(request):
    if request.method == "GET":
        form=CitaForm(request.POST)
        form=CitaForm()
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
    producto = Producto.objects.all()
    return render(request, 'productos.html',{"producto":producto})
