from django.urls import path
from . import views


urlpatterns = [
    # path('servicios/', views.servicios, name="servicios"),
    path('cita/', views.cita, name='cita'),
    path('edicion/', views.edicion, name='edicion'),
    path('evento/', views.evento, name='evento'),
    path('perforacion/', views.perforacion, name='perforacion'),
    path('publicidad/', views.publicidad, name='publicidad'),
    path('productos/', views.producto, name='productos'),
]
