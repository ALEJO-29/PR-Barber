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
    
    
    hora=(
        ('9:00','9:00 am'),
        ('9:30','9:30 am'),
        ('10:00','10:00 am'),
        ('10:30','10:30 am'),
        ('11:00','11:00 am'),
        ('11:30','11:30 am'),
        ('12:00','12:00 am'),
        ('12:30','12:30 pm'),
        ('1:00','1:00 pm'),
        ('1:30','1:30 pm'),
        ('2:00','2:00 pm'),
        ('2:30','2:30 pm'),
        ('3:00','3:00 pm'),
        ('3:30','3:30 pm'),
        ('4:00','4:00 pm'),
        ('4:30','4:30 pm'),
        ('5:00','5:00 pm'),
        ('5:30','5:30 pm'),
        ('6:00','6:00 pm'),
        ('6:30','6:30 pm'),
        ('7:00','7:00 pm'),
    )
    
    fecha = models.DateField(verbose_name="fecha", blank=True, null=True)
    hora = models.TimeField(choices=hora)
    descripcion = models.CharField(max_length=150)
    tipo_corte= models.CharField(max_length=250, choices=tipo_corte, default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
