""" Views de la app services """

from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request): # pylint: disable=unused-argument
    """ vista services """
    services = Service.objects.all() # pylint: disable=redefined-outer-name

    return render(request, "services/services.html", {'services':services})
