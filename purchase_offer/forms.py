from django import forms
from .models import PurchaseOffer

class PurchaseOfferForm(forms.ModelForm):
    class Meta:
        model  = PurchaseOffer
        fields = ("price", "expiration")
        widgets = {
            "price": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "expiration": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
