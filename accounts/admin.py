from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from movies.models import Movie
from .models import GroupProfile


# -----------------------------
# USER ADMIN CUSTOMISATIONS
# -----------------------------

# Show list of groups in the user list
def group_list(obj):
    return ", ".join([g.name for g in obj.groups.all()]) or "—"
group_list.short_description = "Groups"


# Count total movies + clickable link to filtered list
def total_movies(obj):
    count = Movie.objects.filter(user=obj).count()
    url = (
        reverse("admin:movies_movie_changelist")
        + "?"
        + urlencode({"user__id__exact": obj.id})
    )
    return format_html('<a href="{}">{}</a>', url, count)
total_movies.short_description = "Movies"


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        group_list,
        total_movies,
    )

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )


# Replace default User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# -----------------------------
# GROUP ADMIN CUSTOMISATIONS
# -----------------------------

# Member count + clickable link to Users filtered by group
def member_count(obj):
    from django.contrib.auth import get_user_model
    User = get_user_model()

    count = User.objects.filter(groups=obj).count()

    url = (
        reverse("admin:auth_user_changelist")
        + "?"
        + urlencode({"groups__id__exact": obj.id})
    )

    return format_html('<a href="{}">{}</a>', url, count)
member_count.short_description = "Members"


# NEW: Total permissions for each group
def total_permissions(obj):
    return obj.permissions.count()
total_permissions.short_description = "Permissions"


# Inline for editing the GroupProfile description
class GroupProfileInline(admin.StackedInline):
    model = GroupProfile
    can_delete = False
    verbose_name = "Description"
    fk_name = "group"
    fields = ("description",)


# Custom admin for Groups
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ("name", member_count, total_permissions, "get_description")
    inlines = [GroupProfileInline]

    def get_description(self, obj):
        if hasattr(obj, "profile"):
            return obj.profile.description
        return ""
    get_description.short_description = "Description"


# Replace default Group admin
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
