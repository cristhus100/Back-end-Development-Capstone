from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, default="", blank=True)
    lyrics = models.TextField(default="", blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
