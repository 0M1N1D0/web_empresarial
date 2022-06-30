""" Aquí estarán las vistas estáticas """

from django.shortcuts import HttpResponse

# Create your views here.
def home(request): # pylint: disable=unused-argument
    """ vista home """
    return HttpResponse("Inicio")

def about(request): # pylint: disable=unused-argument
    """ vista about """
    return HttpResponse("Historia")

def services(request): # pylint: disable=unused-argument
    """ vista services """
    return HttpResponse("Servicios")

def store(request): # pylint: disable=unused-argument
    """ vista store """
    return HttpResponse("Visítanos")

def contact(request): # pylint: disable=unused-argument
    """ vista contact """
    return HttpResponse("Contacto")

def blog(request): # pylint: disable=unused-argument
    """ vista blog """
    return HttpResponse("Blog")

def sample(request): # pylint: disable=unused-argument
    """ vista sample """
    return HttpResponse("Sample")
