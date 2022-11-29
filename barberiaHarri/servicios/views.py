from django.shortcuts import render, HttpResponse, redirect
from barberApp.models import Cita
from barberApp.models import Producto
from .forms import CitaForm
from django.contrib.auth.models import User
from datetime import date, timedelta
from django import forms
from .carro import Carro
# Create your views here.


def cita(request):
    # mostrat las horas ocupadas en los siguientes 4 dias
    day = date.today()
    enday = day+timedelta(days=4)
    hora = Cita.objects.filter(
        fecha__range=[day, enday]).order_by('fecha', 'hora')

    form = CitaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cita')
    else:
        return render(request, 'cita.html', {'form': form, 'hora': hora})


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
    return render(request, 'productos.html', {"producto": producto})


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect('productos')


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect('productos')


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect('productos')


def limpiar_producto(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect('productos')


    
def total_carro(request):
    total=0
    if request.user.is_authenticated():
        if request.session["carro"]:
            for key, value in request.session["carro"].items():
                total+=total + (float(value["precio"]*value["cantidad"]))
        return {"total_carro": total}