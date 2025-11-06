from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

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
    email = forms.EmailField(required=True, label="New Email")

    class Meta:
        model = User
        fields = ["email"]


class ChangeUsernameForm(forms.ModelForm):
    username = forms.CharField(required=True, label="New Username")

    class Meta:
        model = User
        fields = ["username"]