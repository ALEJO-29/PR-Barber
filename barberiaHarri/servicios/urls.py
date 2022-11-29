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
    #rutas de carro
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_producto, name="CLS"),
]
