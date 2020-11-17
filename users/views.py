from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import LawyerProfile , Review


class SignupView( generic.CreateView ):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy( 'login' )

def displayProfile( request , pk):
    try:
        user = LawyerProfile.objects.get(pk=pk)
    except LawyerProfile.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    #queryset = Post_reply.objects.filter(post_id__pk=pk)

    context = {
        'user' : user
    }

    return render(request, 'profile.html', context)


