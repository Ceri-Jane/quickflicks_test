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

    # Extra info fields
    description = models.TextField(blank=True, null=True)
    release_date = models.CharField(max_length=20, blank=True, null=True)

    # Shelf status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")

    # Rating system: 1 = 👍, -1 = 👎, 0 = no rating
    rating = models.IntegerField(default=0)

    # NEW: Professional timestamp fields (used by admin)
    created_at = models.DateTimeField(auto_now_add=True)   # set on creation
    updated_at = models.DateTimeField(auto_now=True)       # updates every save

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
