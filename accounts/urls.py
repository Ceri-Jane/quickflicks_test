from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", views.signup, name="signup"),

    path("change-email/", views.change_email, name="change_email"),
    path("change-username/", views.change_username, name="change_username"),

    # ✅ Correct user-facing password change route
    path("change-password/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change_form.html",
        success_url="/accounts/change-password/done/",
    ), name="password_change"),

    # ✅ The "password successfully changed" page
    path("change-password/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ), name="password_change_done"),
]
