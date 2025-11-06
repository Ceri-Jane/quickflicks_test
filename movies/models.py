from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    STATUS_CHOICES = [
        ("NEW", "To Put Away"),
        ("TO_WATCH", "To Watch"),
        ("WATCHED", "Watched"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tmdb_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=500, blank=True, null=True)
    
    # ✅ NEW FIELDS
    description = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
