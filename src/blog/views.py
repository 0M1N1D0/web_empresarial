from django.shortcuts import render

# Create your views here.
def blog(request): # pylint: disable=unused-argument
    """ vista blog """
    return render(request, "blog/blog.html")