from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

# add reviews to lawyer profile models

class LawyerProfile( models.Model ):
    user = models.OneToOneField( User , null=True , on_delete = models.CASCADE )
    about = models.TextField()
    firstName = models.CharField(max_length=100 , default = "" )
    lastName = models.CharField(max_length=100, default="")
    speciality = models.CharField(max_length=100 , default = "" )
    court = models.CharField(max_length=100 , default = "" )
    fees = models.CharField(max_length=100 , default = "")
    experience = models.IntegerField( default = 1)
    area = models.CharField(max_length=100 , default = "")



class Review ( models.Model):

    lawyer_id = models.ForeignKey( LawyerProfile, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_added' , )




