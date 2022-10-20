import site
from django.contrib import admin
from .models import Servicio, Producto, TipoProducto, Cita

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Cita)

