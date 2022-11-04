from email.policy import default
from django.db import models

# Create your models here.


class Producto(models.Model):
    imagen = models.ImageField(upload_to="images/", blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    cantidad= models.IntegerField(default=True)
    
    def __str__(self):
        return self. nombre


class TipoProducto(models.Model):
    descripcion = models.CharField(max_length=150)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)


class Servicio(models.Model):
    imagen = models.ImageField(upload_to="images/", blank=True)
    tipo_servicio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tipo_servicio


class Cita(models.Model):
    tipo_corte=(
        ('corte', 'corte'),
        ('cejas', 'cejas'),
        ('barba', 'barba'),
        ('corte y cejas', 'corte y cejas'),
        ('corte y barba', 'corte y barba'),
        ('corte completo', 'corte completo'),
    )
    
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.CharField(max_length=150)
    tipo_corte= models.CharField(max_length=250, choices=tipo_corte, default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
