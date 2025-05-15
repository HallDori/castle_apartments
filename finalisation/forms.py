from django import forms
from .models import Finalisation
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

class ContactForm(forms.ModelForm):
    country = CountryField().formfield(widget=CountrySelectWidget)   # ► select <option>

    class Meta:
        model  = Finalisation
        fields = ["street", "city", "postal", "country", "national_id"]

PAY_CHOICES = (
    ("credit_card", "Credit card"),
    ("bank_transfer", "Bank transfer"),
    ("mortgage", "Mortgage"),
)

class PaymentForm(forms.ModelForm):
    payment_method = forms.ChoiceField(choices=PAY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model  = Finalisation
        fields = ["payment_method",
                  "card_name", "card_number", "card_expiry", "card_cvc",
                  "bank_account", "mortgage_provider"]

    def clean(self):
        cleaned = super().clean()
        pm = cleaned.get("payment_method")

        # wipe irrelevant fields so Review step is tidy
        if pm != "credit_card":
            cleaned.update(card_name="", card_number="", card_expiry="", card_cvc="")
        if pm != "bank_transfer":
            cleaned["bank_account"] = ""
        if pm != "mortgage":
            cleaned["mortgage_provider"] = ""

        # basic req. validation
        if pm == "credit_card" and not cleaned["card_number"]:
            self.add_error("card_number", "Required for credit-card payment.")
        if pm == "bank_transfer" and not cleaned["bank_account"]:
            self.add_error("bank_account", "Bank account required.")
        if pm == "mortgage" and not cleaned["mortgage_provider"]:
            self.add_error("mortgage_provider", "Choose your mortgage provider.")

        return cleaned

class ReviewForm(forms.Form):
    pass