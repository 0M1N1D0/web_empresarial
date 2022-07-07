""" Aquí estarán las vistas estáticas """

from django.shortcuts import render

# Create your views here.
def home(request): # pylint: disable=unused-argument
    """ vista home """
    return render(request, "vista/home.html")

def about(request): # pylint: disable=unused-argument
    """ vista about """
    return render(request, "vista/about.html")

def store(request): # pylint: disable=unused-argument
    """ vista store """
    return render(request, "vista/store.html")

def contact(request): # pylin: disable=unused-argument
    """ vista contact """
    return render(request, "vista/contact.html")

def sample(request): # pylint: disable=unused-argument
    """ vista sample """
    return render(request, "vista/sample.html")
