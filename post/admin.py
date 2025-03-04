from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)
