from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView
from .models import Post
from .forms import PostForm , PostCreateForm


class HomeView( ListView ):
    model = Post
    template_name = 'home.html'

class ArticleDetailView( DetailView):
    model = Post
    template_name = 'details.html'

class CreatePost ( CreateView):
    model = Post
    form_class = PostForm
    template_name= 'create_post.html'
    #fields  = '__all__'


def create_post(request) :

    form = Post (request.POST or None)
    context = {
        'form_': form
    }

    if request.method == 'POST':

        if form.is_valid():
            publish = form.save(commit=False)
            #publish.author = request.user
            publish.save()

    return render(request, 'create_p.html', context )


class CreatePost2 ( CreateView):
    model = Post
    form_class = PostCreateForm
    template_name= 'create_post.html'
    #fields  = '__all__'

    def form_valid(self, form):
       form.instance.author = self.request.user
       return super( CreatePost2 , self).form_valid(form)


"""
def product_detail( request ):

    obj = Post.objects.get(id =1 )
    context = {
        'post' =obj
    }

    return render(request ,)

"""