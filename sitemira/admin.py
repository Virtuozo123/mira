from django.contrib import admin

from .models import create, Comment, blog

admin.site.register(create)
admin.site.register(Comment)
admin.site.register(blog)