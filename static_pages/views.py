from django.shortcuts import render
from posts.models import Post
from users.models import LawyerProfile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound ,  HttpResponseRedirect
# Create your views here.


def trueHome(request ):
    try:
        post = Post.objects.all()[0:3]
    except Post.DoesNotExist:
        pass

    context = {
        'posts': post
    }

    return render(request, 'static_home.html', context)

def about_us(request ):

    return render(request, 'about.html', {})
