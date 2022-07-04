""" Config admin de la app services """

from django.contrib import admin
from .models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    """ Clase admin para el modelo Service """
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
