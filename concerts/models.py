from django.db import models
from datetime import datetime


class Concert(models.Model):
    concert_name = models.CharField(max_length=255)
    event_date = models.DateField(default=datetime.now)
    venue = models.CharField(max_length=255, default="")
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.concert_name
