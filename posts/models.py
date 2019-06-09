from django.db import models

# Create your models here.
class User(models.Model):
    #Modelo de usuario 
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    bio = models.TextField()
    birthdate = models.DateTimeField(blank=True,null=True) #Start blank and admit null 
    created = models.DateTimeField(auto_now_add=True) #Save at create
    modified = models.DateTimeField(auto_now=True) #Save at edit
    is_admin = models.BooleanField(default=False)