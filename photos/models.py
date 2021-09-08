from django.db import models
from django.utils import timezone


class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pics')
    date_posted = models.DateTimeField(default=timezone.now)
