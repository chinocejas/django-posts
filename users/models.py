from django.db import models
#Users imports 
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #proxy model that extend the base data with other information 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(max_length = 100, blank = True)
    biographi =  models.TextField(blank = True)
    phone_number = models.CharField(max_length = 20,blank = True)
    profile_picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
