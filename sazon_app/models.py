from django.db import models

# Create your models here.
class inventario(models.Model):
    producto = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    disponible = models.IntegerField()
    observacion = models.CharField(max_length=255)
        
def _srt_(self):
        return self.inventario

class gerente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    contacto = models.CharField(max_length=20)
    
    def _srt_(self):
        return self.gerente

        