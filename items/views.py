from datetime import datetime
from nis import cat
from pickle import NONE
from tkinter import ON
from tkinter.tix import Tree
from typing_extensions import Self
from xml.etree.ElementTree import Element
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count, Q
from django.urls import reverse
from django.utils import timezone

from items.models import item , categoria, usuario, prestamo


# Create your views here.


def index(request):
    print('Request para index')

    items = item.objects.order_by("disponible")
    usuarios = usuario.objects.all()
    prestamos = prestamo.objects.all()
    categorias = categoria.objects.all()

    arreglo = []
    for caca in items:
        if caca.disponible == False:
            prestamo_aux = prestamos.filter(item__id = caca.id, devuelto = False).first()
            xd = caca , prestamo_aux.usuario, prestamo_aux.fecha_prestamo
            arreglo.append(xd)
        
        else:
            xd = caca, '',''
            arreglo.append(xd)

    return render(request, 'index.html', {'items': arreglo, 'usuarios':usuarios, 'prestamos':prestamos, 'categorias':categorias})



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
        items = items.filter(categoria__categoria = 'juego')

    elif (chek_3 != None and chek_4 == None):
        items = items.filter(categoria__categoria = 'computador')

    elif (chek_3 == None and chek_4 == None):
        items = items.filter(categoria = '')

    usuarios = usuario.objects.all()
    prestamos = prestamo.objects.all()
    categorias = categoria.objects.all()

    arreglo = []
    for caca in items:
        if caca.disponible == False:
            prestamo_aux = prestamos.filter(item__id = caca.id, devuelto = False).first()
            xd = caca , prestamo_aux.usuario, prestamo_aux.fecha_prestamo
            arreglo.append(xd)
        
        else:
            xd = caca, '',''
            arreglo.append(xd)
    
    


    return render(request, 'index.html', {'items': arreglo, 'casillas': casillas, 'usuarios':usuarios, 'prestamos':prestamos, 'categorias':categorias})


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

    usuarios = usuario.objects.all()
    prestamos = prestamo.objects.all()
    categorias = categoria.objects.all()

    arreglo = []
    for caca in items:
        if caca.disponible == False:
            prestamo_aux = prestamos.filter(item__id = caca.id, devuelto = False).first()
            xd = caca , prestamo_aux.usuario, prestamo_aux.fecha_prestamo
            arreglo.append(xd)
        
        else:
            xd = caca, '',''
            arreglo.append(xd)

    return render(request, 'index.html', {'items': arreglo, 'usuarios':usuarios, 'prestamos':prestamos, 'categorias':categorias})



def prestar(request):
    print('Request para prestar')

    item_id= request.POST.get('itemid')
    rol = request.POST.get('user_name')

    print("id del item: ",item_id)

    elemento = get_object_or_404(item, pk=item_id)

    user = usuario.objects.filter(rol=rol).first()

    if(user):
        print(elemento)
        print(user)

        prestamo_ = prestamo(usuario = user, item = elemento, fecha_prestamo = timezone.now())
        prestamo_.save()

        elemento.disponible = False
        item.save(elemento)

    else:
        items = item.objects.order_by("disponible")
        usuarios = usuario.objects.all()
        prestamos = prestamo.objects.all()
        categorias = categoria.objects.all()

        arreglo = []
        for caca in items:
            if caca.disponible == False:
                prestamo_aux = prestamos.filter(item__id = caca.id, devuelto = False).first()
                xd = caca , prestamo_aux.usuario, prestamo_aux.fecha_prestamo
                arreglo.append(xd)
            
            else:
                xd = caca, '',''
                arreglo.append(xd)

        return render(request, 'index.html', {'items': arreglo, 'usuarios':usuarios, 'prestamos':prestamos, 'categorias':categorias, 'mensaje_alerta':'usuario no encontrado'})

    return HttpResponseRedirect(reverse('index'))



def devolver(request):
    print('Request para devolver')

    item_id= request.POST.get('itemidd')
    elemento = get_object_or_404(item, pk=item_id)
    elemento_prestamo = prestamo.objects.filter(item=elemento, devuelto = False).first()

    elemento_prestamo.fecha_devuelto = timezone.now()
    elemento_prestamo.devuelto = True
    prestamo.save(elemento_prestamo)

    elemento.disponible = True
    item.save(elemento)

    return HttpResponseRedirect(reverse('index'))

def agregar(request):
    print("request agregar")

    return(render(request, 'agregar_item.html'))

def agregar_item(request):
    print("request agregar_item")

    nombre = request.POST.get('nombre')
    codigo = request.POST.get('codigo')
    categoria_ = request.POST.get('categoria')
    description = request.POST.get('comentario')

    categoria_aux = categoria.objects.filter(categoria=categoria_).first()

    item_ = item(nombre = nombre, codigo=codigo, categoria = categoria_aux, description = description, disponible=True)
    item_.save()

    mensaje = str(nombre)+ ' agregado correctamente '


    return(render(request, 'agregar_item.html', {'mensaje':mensaje}))
