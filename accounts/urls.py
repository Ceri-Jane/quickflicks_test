from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),

    # Login uses our moved template
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),

    # Logout and bounce to home (we already set LOGOUT_REDIRECT_URL = "/")
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Signup (wired in next step)
    path("signup/", views.signup, name="signup"),
]
