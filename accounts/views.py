from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
