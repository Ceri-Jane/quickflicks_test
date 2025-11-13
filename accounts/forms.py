from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "required": "required",
            "type": "email",
            "placeholder": "Enter your email"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ChangeEmailForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="New Email",
        widget=forms.EmailInput(attrs={
            "required": "required",
            "type": "email",
            "placeholder": "Enter a valid email address"
        })
    )

    class Meta:
        model = User
        fields = ["email"]


class ChangeUsernameForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label="New Username",
        widget=forms.TextInput(attrs={
            "type": "text",
            "required": "required",
            "minlength": "3",
            "maxlength": "20",
            "pattern": "^[A-Za-z0-9_]{3,20}$",
            "title": "Username must be 3–20 characters and contain only letters, numbers, or underscores.",
            "placeholder": "Choose a username"
        })
    )

    class Meta:
        model = User
        fields = ["username"]
