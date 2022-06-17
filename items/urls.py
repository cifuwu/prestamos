from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filtro', views.filtro, name='filtro'),
    path('buscar', views.buscar, name='buscar'),
    path('prestar', views.prestar, name='prestar'),
    path('devolver', views.devolver, name='devolver'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_item', views.agregar_item, name='agregar_item'),
    path('<int:id>/', views.item_, name='item_'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('agregar_usuario', views.agregar_usuario, name='agregar_usuario'),
    path('agregar_usuario_', views.agregar_usuario_, name='agregar_usuario_'),
]
handler404 = 'items.views.view_404'
