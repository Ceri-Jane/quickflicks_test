# accounts/forms_reset.py

from django import forms
from django.contrib.auth.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    """
    Extends Django’s PasswordResetForm so we can apply
    HTML5 validation attributes (required, type=email, pattern, etc.)
    without showing visible form code in the template.
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "type": "email",
            "required": "required",
            "autocomplete": "email",
            "pattern": r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
            "title": "Please enter a valid email address",
            "placeholder": "Enter your account email"
        })
    )
