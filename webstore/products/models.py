from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre