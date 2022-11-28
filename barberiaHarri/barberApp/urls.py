from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reporte/', views.reporte, name="reporte"),
    path('reporteExcel/', views.reporte_excel.as_view(), name="reporteExcel"),
]
