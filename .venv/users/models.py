from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

#Profile model, linked to User
#Model creation form turtorial [6] (see references)
class Profile(models.Model):
    #If user is deleted, delete the profile 1 - 1
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


