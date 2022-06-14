from datetime import datetime
from pickle import NONE
from tkinter import ON
from typing_extensions import Self
from xml.etree.ElementTree import Element
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count, Q
from django.urls import reverse
from django.utils import timezone

from items.models import item


# Create your views here.


def index(request):
    print('Request para index')

    items = item.objects.order_by("disponible")


    return render(request, 'index.html', {'items': items})



def filtro(request):
    print('Request para filtro')

    chek_1 = request.POST.get('Check-1')
    chek_2 = request.POST.get('Check-2')
    chek_3 = request.POST.get('Check-3')
    chek_4 = request.POST.get('Check-4')

    casillas = [chek_1, chek_2, chek_3, chek_4]
    print(casillas, '\n')

    if (chek_1 != None and chek_2 != None):
        items = item.objects.order_by("disponible")
    
    elif (chek_1 == None and chek_2 != None):
        items = item.objects.filter(disponible = False)
        
    elif (chek_1 != None and chek_2 == None):
        items = item.objects.filter(disponible = True)
    
    else:
        items = item.objects.filter(categoria = '')



    if (chek_3 == None and chek_4 != None):
        items = items.filter(categoria = 'juego')

    elif (chek_3 != None and chek_4 == None):
        items = items.filter(categoria = 'computador')

    elif (chek_3 == None and chek_4 == None):
        items = items.filter(categoria = '')
    


    return render(request, 'index.html', {'items': items, 'casillas': casillas})


def buscar(request):
    print('Request para busqueda')

    busqueda = request.POST.get('busqueda')

    def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s
    
    busqueda = normalize(busqueda)

    items = item.objects.filter(Q(nombre__icontains = busqueda))


    return render(request, 'index.html', {'items': items})


def prestar(request):
    print('Request para prestar')

    item_id= request.POST.get('itemid')
    nombre = request.POST.get('user_name')

    #print("id del item: ",item_id)

    elemento = get_object_or_404(item, pk=item_id)

    print(elemento)

    elemento.disponible = False
    elemento.fecha_prestamo = timezone.now()
    elemento.usuario = nombre
    item.save(elemento)


    items = item.objects.order_by("disponible")

    return render(request, 'index.html', {'items': items})


def devolver(request):
    print('Request para devolver')

    item_id= request.POST.get('itemidd')
    elemento = get_object_or_404(item, pk=item_id)


    elemento.disponible = True
    item.save(elemento)

    items = item.objects.order_by("disponible")

    return render(request, 'index.html', {'items': items})


