from django.contrib import admin
from .models import Profile

# Registering Profile to view/update/delete from admin page
admin.site.register(Profile)
