from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
