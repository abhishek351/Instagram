from django.contrib import admin
from .models import post,profile,Comment,Notification

# Register your models here.
admin.site.register(post)
admin.site.register(profile)
admin.site.register(Notification)
admin.site.register(Comment)
