from django.db import models

# Create your models here.

class user(models.Model):

    account   = models.CharField(max_length=30)
    name      = models.CharField(max_length=10)
    passwd    = models.CharField(max_length=32)
    facePhoto = models.CharField(max_length=100)
    identity  = models.ImageField(max_length=1)
    token     = models.CharField(max_length=50)
    isDelete  = models.BooleanField(default=False)

class grouplist(models.Model):
    groupid   = models.ForeignKey()

