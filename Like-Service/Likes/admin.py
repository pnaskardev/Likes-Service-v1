from django.contrib import admin

from . models import PostEvent, LikeEvent

admin.site.register(LikeEvent)
admin.site.register(PostEvent)
