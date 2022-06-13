from django.db import models

# Create your models here.


class item(models.Model):
    categorias = (('computador', 'computador'), ('juego', 'juego'), ('otros', 'otros'), ('accesorios', 'accesorios'))

    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100, choices=categorias)
    description = models.CharField(max_length=250, blank=True)
    usuario = models.CharField(max_length=100, blank=True)
    comentario = models.CharField(max_length=500, blank=True)
    fecha_prestamo = models.DateTimeField('fecha prestamo', null=True, blank=True)   
    disponible = models.BooleanField()

    def __str__(self):
        return self.nombre

    def ver_categoria(self):
        return str(self.categoria)

    def ver_usuario(self):
        return str(self.usuario)



