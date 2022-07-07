from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request): # pylint: disable=unused-argument
    """ vista blog """
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})