from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True)
    image_url = models.URLField(max_length=500, default="", blank=True)

    def __str__(self):
        return self.title
