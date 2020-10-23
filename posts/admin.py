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


admin.site.register(Post_reply)