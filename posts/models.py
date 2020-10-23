from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField

#To Do:-
# add togs or category models
# remove title tag
# create side bar
# add pagination
#add likes

class Post( models.Model):
    STATUS_CHOICES = (
        ('created' , 'Created')
    )

    title = models.CharField( max_length = 250 )
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey( User , on_delete=models.CASCADE )
    #body = models.TextField()
    body = RichTextField   ( blank=True , null=True)
    #publish = models.DateTimeField( auto_now_add = True , name='date published')
    created = models.DateTimeField( default= timezone.now )

    slug = models.SlugField( max_length= 300 , unique_for_date='created' )

    likes = models.ManyToManyField( User , related_name='post_likes')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title # + ' | ' + str(self.author)

    def get_absolute_url(self):
        #print((self.id))
        return reverse('post-details' , args=(self.pk , ))


class Post_reply (models.Model):
    title_tag = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey( Post , on_delete=models.CASCADE)
    body = models.TextField()



