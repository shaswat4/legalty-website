
from django import forms
from .models import LawyerProfile
from django.contrib.auth.models import User


class LawyerDetailForm ( forms.ModelForm):
    class Meta :
        model = LawyerProfile
        fields = [
            'firstName' ,
            'lastName' ,
            'speciality',
            'court' ,
            'fees' ,
            'experience',
            'area' ,
            'about'
        ]

        widgets = {

            'firstName' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastName' : forms.TextInput(attrs={'class': 'form-control'}),
            'speciality' : forms.TextInput(attrs={'class': 'form-control'}),
            'court' : forms.TextInput(attrs={'class': 'form-control'}),
            'fees' : forms.TextInput(attrs={'class': 'form-control'}),
            'experience' : forms.TextInput(attrs={'class': 'form-control'}),
            'area' : forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),

            #'title' : forms.TextInput( attrs= {'class' : 'form-control', 'placeholder':'please write yur title'}),
            #'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = []