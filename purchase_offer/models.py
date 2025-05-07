from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from property.models import Property

class PurchaseOffer(models.Model):
    PENDING     = "pending"
    ACCEPTED    = "accepted"
    REJECTED    = "rejected"
    CONTINGENT  = "contingent"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
        (CONTINGENT, "Contingent"),
    ]

    property   = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="offers")
    buyer      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="offers")
    price      = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    expiration = models.DateField()
    status     = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("property", "buyer")
        ordering = ("-created",)

    def __str__(self):
        return f"Offer {self.price} on {self.property} by {self.buyer}"


# --- attach helper back‑reference without circular import -----------------
def _property_is_sold(self):
    return self.offers.filter(status=PurchaseOffer.ACCEPTED).exists()

Property.is_sold = property(_property_is_sold)   # monkey‑patch once models are ready