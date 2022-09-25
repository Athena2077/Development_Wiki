from django.contrib import admin
from .models import Post , Categories

#Models past through to admin page, for admin to creat/update/delte if needed.
admin.site.register(Post)
admin.site.register(Categories)