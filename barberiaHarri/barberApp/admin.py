import site
from django.contrib import admin
from .models import  Producto, TipoProducto, Cita, Usuario

# Register your models here.

admin.site.site_header = 'Barber Harry'
admin.site.index_title = 'Panel de control Barber Harry'
admin.site.site_title = 'Administrador de la pagina'

admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Cita)
admin.site.register(Usuario)

