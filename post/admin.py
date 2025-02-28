from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')

admin.site.register(Video, VideoAdmin)
