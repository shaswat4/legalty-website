from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.urls import reverse_lazy
from .models import LawyerProfile , Review
from .forms import  LawyerDetailForm
from django.http import HttpResponse, HttpResponseNotFound ,  HttpResponseRedirect
from django.views.generic import ListView , DetailView


class SignupView( generic.CreateView ):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy( 'login' )

class CreateLawyerProfile ( generic.CreateView ):
    model = LawyerProfile
    form_class = LawyerDetailForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy( 'home' )

    #def get_success_url(self):
    #    return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def form_valid(self, form):
        form.instance.user = self.request.user
        print("saved")
        return super(CreateLawyerProfile, self).form_valid(form)

class EditLawyerProfile ( generic.edit.UpdateView ):
    model = LawyerProfile
    form_class = LawyerDetailForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy( 'home' )

    #def get_success_url(self):
    #    return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def form_valid(self, form):
        print("saved")
        return super(EditLawyerProfile , self).form_valid(form)

def edit (request , pk ):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        lawyer_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user_form.save()
            lawyer_form.save()


def displayProfile( request , pk):
    try:
        form = LawyerProfile.objects.get(pk=pk)
    except LawyerProfile.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    #queryset = Post_reply.objects.filter(post_id__pk=pk)

    context = {
        'form' : form
    }

    return render(request, 'profile.html', context)


'''
class detailLawyer( DetailView ):
    model = LawyerProfile
    template = 'profile.html'
'''