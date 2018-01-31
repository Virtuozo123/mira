from django.contrib import admin

from .models import create, Comment

admin.site.register(create)
admin.site.register(Comment)
