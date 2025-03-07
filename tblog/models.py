import datetime
from os import truncate

from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils import timezone
from django.utils.text import Truncator
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="tblog/images/")
    content = models.TextField()
    tags = models.CharField(max_length=255, help_text="Comma-separated tags")
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def is_recent_post(self):
        return self.date >= timezone.now() - datetime.timedelta(days=5)

    @property
    def is_today(self):
        return self.date == timezone.now().date()

    @property
    def excerpt(self):
        return Truncator(self.content).words(30)
