from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class LawyerProfile( models.Model ):
    user = models.OneToOneField( User , null=True , on_delete = models.CASCADE )
    about = models.TextField()


class Review ( models.Model):
    lawyer_id = models.ForeignKey( LawyerProfile, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('date_added' , )




