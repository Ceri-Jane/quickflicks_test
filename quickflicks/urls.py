from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Import your custom reset form
from accounts.forms_reset import CustomPasswordResetForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django's built-in login/logout/password reset (kept as-is)
    path('accounts/', include('django.contrib.auth.urls')),

    # Your custom auth routes (signup, profile, etc)
    path('accounts/', include('accounts.urls')),

    # Styled Password Reset pages using your new form
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset.html",
        form_class=CustomPasswordResetForm  # ← ★ IMPORTANT ★
    ), name="password_reset"),

    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ), name="password_reset_complete"),

    # Movie pages
    path('', include('movies.urls')),
]
