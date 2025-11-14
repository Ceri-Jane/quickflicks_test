from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    # -------- LIST VIEW DISPLAY --------
    list_display = (
        "thumbnail",        # poster (with fallback)
        "title",
        "user",
        "status_badge",
        "rating_display",
        "tmdb_id",
        "created_at",
    )

    list_filter = (
        "status",
        "rating",
        "user",
        "created_at",
    )

    search_fields = (
        "title",
        "tmdb_id",
        "user__username",
    )

    ordering = ("-created_at",)

    # -------- FIELDSET LAYOUT --------
    fieldsets = (
        ("Movie Information", {
            "fields": ("title", "tmdb_id", "poster_url")
        }),
        ("Shelf & Status", {
            "fields": ("user", "status", "rating")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

    # -------- CUSTOM DISPLAY METHODS --------
    def thumbnail(self, obj):
        """
        Show valid TMDB poster OR fallback image when:
        - poster_url is empty
        - poster_url is 'None'
        - poster_url ends with 'None'
        - poster_url is not a valid URL
        """

        url = (obj.poster_url or "").strip()

        # ❌ Detect TMDB broken poster URLs like:
        # https://image.tmdb.org/t/p/w200None
        if not url or url.endswith("None"):
            url = ""  # force fallback

        # ✔️ Valid URL → use real image
        if url.startswith("http://") or url.startswith("https://"):
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;" />',
                url
            )

        # ✔️ Fallback image
        fallback_url = static("images/movie-poster-unavailable.jpg")
        return format_html(
            '<img src="{}" style="height:60px; border-radius:4px; opacity:0.9;" />',
            fallback_url
        )

    thumbnail.short_description = "Poster"

    def rating_display(self, obj):
        if obj.rating == 1:
            return "👍"
        elif obj.rating == -1:
            return "👎"
        return "Not yet rated"

    rating_display.short_description = "Rating"

    def status_badge(self, obj):
        color_map = {
            "NEW": "gray",
            "TO_WATCH": "blue",
            "WATCHED": "green",
        }
        color = color_map.get(obj.status, "gray")
        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.get_status_display(),
        )

    status_badge.short_description = "Status"
