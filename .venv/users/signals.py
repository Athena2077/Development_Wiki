from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#Creates profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#Saves profile when changed 
@receiver(post_save, sender=User)
def saves_profile(sender, instance, created, **kwargs):
    instance.profile.save()

