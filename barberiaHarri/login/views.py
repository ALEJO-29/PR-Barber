from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UsuarioForm

# Create your views here.


# clase de registro
class RegistroUser(View):

    # mostrar el formulario de registro
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'singup.html', {'form': form})

    # validar el registro
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect('formularioUser')
        else:
            return render(request, 'singup.html', {'form': form})


# cerrar la sesion
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

# validar el logueo


def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('usuario no valido')
        else:
            return render(request, 'login.html', {'form': form})


# formulario para usuarios
def Usuario(request):
    form = UsuarioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'formularioUser.html', {'form': form})