from pyexpat import model
from django.db import models

# Create your models here.


class categoria(models.Model):
    categoria = models.CharField(max_length=50)
    logo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.categoria
        

class usuario(models.Model):
    nombre = models.CharField(max_length=150)
    rol = models.CharField(max_length=15, blank=True)
    rut = models.CharField(max_length=15, blank=True)
    correo = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-nombre']


class item(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, blank=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True)
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre

    def ver_categoria(self):
        return str(self.categoria)



class prestamo(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField('fecha prestamo', null=True, blank=True)   
    fecha_devuelto = models.DateTimeField('fecha devuelto', null=True, blank=True)   
    devuelto = models.BooleanField(default=False)


    def __str__(self):
        return str(self.item)+'  |  '+str(self.usuario.nombre)
