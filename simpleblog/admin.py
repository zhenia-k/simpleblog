from django.contrib import admin
from django.contrib import admin

from .models import Post, Comment, Profile, Message


admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
admin.site.register(Profile)
admin.site.register(Message)