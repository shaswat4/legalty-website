from django.contrib import admin
from .models import Post , Post_reply
# Register your models here.

@admin.register(Post)
class PostAdmin( admin.ModelAdmin ):
    list_display = (
        'title' , 'slug' , 'author' , 'created'
    )
    list_filter = ('title' , 'created' , 'author'  )
    search_fields = ( 'title'  , 'body' , 'author')
    prepopulated_fields = { 'slug':('title' , )  }


#admin.site.register(Post_reply)

@admin.register(Post_reply)
class CommentAdmin( admin.ModelAdmin ):
    list_display = ( 'author' , 'post_id', 'date_added' , 'body')
    list_filter = ('date_added' , )
    search_fields = ('author' , 'body')