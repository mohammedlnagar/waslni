from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, UserProfile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


import re  # For mobile number validation

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser
import re  # For mobile number validation

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mobile_number = forms.CharField(
        required=True,
        max_length=15,
        help_text="Enter a valid phone number.",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. Please choose another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered. Use a different one.")
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get("mobile_number")
        if not re.match(r'^\+?[1-9]\d{6,14}$', mobile_number):  # International format
            raise ValidationError("Enter a valid mobile number (e.g., +123456789).")
        if CustomUser.objects.filter(mobile_number=mobile_number).exists():
            raise ValidationError("This mobile number is already registered.")
        return mobile_number



class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "mobile_number"]


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "passport",
            "emirates_id",
            "university_certificate",
            "cv",
            "role",
            "work_email",
            "home_address",
            "marital_status",
            "visa_copy",
            "birthdate",
            "emergency_contact_name",
            "emergency_contact_phone",
            "nationality",
        ]
        widgets = {
            "birthdate": forms.DateInput(attrs={"type": "date"}),
        }
