from django.urls import path
from . import views


urlpatterns = [
    path('singup/', views.RegistroUser.as_view(), name="singup"),
    path('logout/', views.cerrar_sesion, name="cerrar_sesion"),
    path('login/', views.login_user, name="login"),
    path('formularioUser/', views.Usuario, name="formularioUser"),
]
