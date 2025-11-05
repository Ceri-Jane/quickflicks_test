from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tmdb_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'Watched' if self.watched else 'Not Watched'})"
