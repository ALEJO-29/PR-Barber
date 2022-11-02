from django.urls import path
from . import views

urlpatterns = [
    path('Acerca pueblorrico/', views.nosotros,name='nosotros' )
]
