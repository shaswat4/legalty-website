
from django.urls import path
from .views import HomeView , ArticleDetailView , CreatePost , create_post , CreatePost2

urlpatterns = [
    path('' , HomeView.as_view() , name='home') ,
    path ( 'a/<int:pk>' ,  ArticleDetailView.as_view() , name='article-details' ) ,
    path('create/' , CreatePost.as_view()  , name='create_post' ) ,
    path('c/' , CreatePost2.as_view() , name='cp' ) ,
]
