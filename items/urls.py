from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtro', views.filtro, name='filtro'),
    path('buscar', views.buscar, name='buscar'),
    path('prestar', views.prestar, name='prestar'),
    path('devolver', views.devolver, name='devolver'),
]