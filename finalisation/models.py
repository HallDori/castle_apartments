from django.db import models
from django.utils import timezone

from purchase_offer.models import PurchaseOffer


class Finalisation(models.Model):
    CREDIT_CARD     = "credit_card"
    BANK_TRANSFER   = "bank_transfer"
    MORTGAGE        = "mortgage"

    PAY_CHOICES = [
        (CREDIT_CARD,   "Credit card"),
        (BANK_TRANSFER, "Bank transfer"),
        (MORTGAGE,      "Mortgage"),
    ]

    offer = models.OneToOneField(
        PurchaseOffer, on_delete=models.CASCADE, related_name="finalisation"
    )

    # Contact
    street      = models.CharField(max_length=255)
    city        = models.CharField(max_length=100)
    postal      = models.CharField(max_length=20)
    country     = models.CharField(max_length=56)
    national_id = models.CharField(max_length=20)

    # Payment
    payment_method   = models.CharField(max_length=13, choices=PAY_CHOICES)
    card_name        = models.CharField(max_length=255, blank=True)
    card_number      = models.CharField(max_length=19, blank=True)
    card_expiry      = models.CharField(max_length=5,  blank=True)
    card_cvc         = models.CharField(max_length=4,  blank=True)
    bank_account     = models.CharField(max_length=34, blank=True)
    mortgage_provider = models.CharField(max_length=255, blank=True)

    confirmed     = models.BooleanField(default=False)
    confirmed_at  = models.DateTimeField(null=True, blank=True)

    def confirm(self):
        self.confirmed = True
        self.confirmed_at = timezone.now()
        self.save(update_fields=["confirmed", "confirmed_at"])

    def __str__(self):
        return f"Finalisation for {self.offer}"