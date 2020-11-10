from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView
from .models import Post , Post_reply
from .forms import PostForm , PostCreateForm , Post_replyCreateForm
from django.http import HttpResponse, HttpResponseNotFound



class HomeView( ListView ):
    model = Post
    template_name = 'home.html'
    paginate_by = 8


class ArticleDetailView( DetailView):
    model = Post
    template_name = 'details.html'

def postDetails(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    queryset = Post_reply.objects.filter( post_id__pk = pk )

    context = {
        'post': post ,
        'replyset' : queryset
    }

    return render(request, 'details.html', context)


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


class CreateReply ( CreateView):
    model = Post_reply
    form_class = Post_replyCreateForm
    template_name= 'create_comment.html'
    #fields  = '__all__'

    def form_valid(self, form):
       form.instance.author = self.request.user
       print( dir(self.request) )
       #form.instance.post_id = self.request.comments

       return super( CreateReply , self).form_valid(form)


def display_post_details(request, pk):
    form = Post_replyCreateForm( request.POST or None)

    if form.is_valid():
        form.instance.author = request.user
        form.instance.post_id = Post.objects.get(pk=pk)
        form.save()
        form = Post_replyCreateForm()

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found")

    queryset = Post_reply.objects.filter(post_id__pk=pk)

    context = {
        'post': post,
        'form' : form ,
        'replyset': queryset
    }

    return render(request, 'details_post_and_reply.html', context)



"""
def product_detail( request ):

    obj = Post.objects.get(id =1 )
    context = {
        'post' =obj
    }

    return render(request ,)

"""