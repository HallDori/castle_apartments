# user/forms.py
from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ("first_name", "last_name", "profile_image")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name":  forms.TextInput(attrs={"class": "form-control"}),
            "profile_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
