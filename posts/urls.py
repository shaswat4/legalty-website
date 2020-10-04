
from django.urls import path
from .views import HomeView , ArticleDetailView  , create_post , CreatePost2 , postDetails

urlpatterns = [
    path('' , HomeView.as_view() , name='home') ,
    path ( 'a/<int:pk>' ,  ArticleDetailView.as_view() , name='article-details' ) ,
   # path('create/' , CreatePost.as_view()  , name='create_post' ) ,
    path('create/' , CreatePost2.as_view() , name='create_post' ) ,
    path ( 'p/<int:pk>' ,  postDetails , name= 'post-details' ) ,
]
