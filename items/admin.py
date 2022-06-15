from django.contrib import admin
from .models import item , categoria, usuario, prestamo

# Register your models here.

admin.site.register(item)
admin.site.register(categoria)
admin.site.register(usuario)
admin.site.register(prestamo)
