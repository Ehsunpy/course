from django.db import models
from embed_video.fields import EmbedVideoField
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    youtube_url = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        