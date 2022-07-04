""" Modelos de la app services  """

from django.db import models

# Create your models here.
class Service(models.Model):
    """ modelo Service """
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta: # pylint: disable=too-few-public-methods
        """ Clase Meta del modelo Service """
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self): # pylint: disable=invalid-str-returned
        return self.title
