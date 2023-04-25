from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    password = models.CharField(max_length=500)
    

class Song(models.Model):
    songname = models.CharField(max_length = 150, null=False, blank = False)
    songimage = models.ImageField(upload_to = 'image')
    songaudio = models.FileField(upload_to= 'audio')
    singer = models.CharField(max_length= 2000)
    songmoviename = models.CharField(max_length = 150, default = "None")
    uploaded= models.DateTimeField(auto_now_add = True)
        
class Track(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=300)    