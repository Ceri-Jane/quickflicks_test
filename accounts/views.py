from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, ChangeEmailForm, ChangeUsernameForm


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def change_email(request):
    if request.method == "POST":
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Email updated successfully ✅")
            return redirect("profile")
    else:
        form = ChangeEmailForm(instance=request.user)

    return render(request, "accounts/change_email.html", {"form": form})


@login_required
def change_username(request):
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Username updated!")
            return redirect("profile")
    else:
        form = ChangeUsernameForm(instance=request.user)

    return render(request, "accounts/change_username.html", {"form": form})