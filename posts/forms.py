
from django import forms
from .models import Post , Post_reply

class PostForm ( forms.ModelForm):
    class Meta :
        model = Post
        fields = {'title','title_tag', 'author','body'}

        widgets = {
            'title' : forms.TextInput( attrs= {'class' : 'form-control', 'placeholder':'please write yur title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostCreateForm ( forms.ModelForm):
    class Meta :
        model = Post
        fields = {'title','title_tag','body'}

        widgets = {
            'title' : forms.TextInput( attrs= {'class' : 'form-control', 'placeholder':'please write yur title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class Post_replyCreateForm ( forms.ModelForm):
    class Meta:
        model = Post_reply
        fields = { 'body' }

    widgets = {
        'body': forms.Textarea(attrs={'class': 'form-control'})
    }
