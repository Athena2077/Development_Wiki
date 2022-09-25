from dataclasses import field
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Models for app 

#Categories model, for user to select when creating a new post/filter on.
class Categories(models.Model):
    category = models.CharField(max_length=100)

    #Returning category to see selections in drop down, instead of category(1), category(2) etc. 
    def __str__(self):
        return self.category

#Post model, used to create new posts within the app
#Model creation form turtorial [5] (see references)
class Post(models.Model):
    title = models.CharField(max_length=100)
    #Category model used to link categories
    category = models.ForeignKey("Categories", on_delete=models.CASCADE, )
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #Using the inbuilt User model to link post to logged in user.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #Returning title as self
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


        