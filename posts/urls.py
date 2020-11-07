
from django.urls import path
from .views import HomeView , ArticleDetailView  , create_post , CreatePost2 , postDetails , CreateReply , display_post_details

urlpatterns = [
    path('' , HomeView.as_view() , name='home') ,
    path ( 'a/<int:pk>' ,  ArticleDetailView.as_view() , name='article-details' ) ,
   # path('create/' , CreatePost.as_view()  , name='create_post' ) ,
    path('create/' , CreatePost2.as_view() , name='create_post' ) ,
    path ( 'p/<int:pk>' ,  postDetails , name= 'post-details' ) ,
    path ( 'p/<int:pk>/comment' , CreateReply.as_view() , name= 'create-reply') ,
    path ( 'post/<int:pk>' ,  display_post_details , name= 'details-post-and-reply' ) ,
]
