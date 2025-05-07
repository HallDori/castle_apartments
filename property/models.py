from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

from seller.models import Seller     # local import is OK here

class Property(models.Model):
    VILLA      = "villa"
    HOUSE      = "house"
    TOWNHOUSE  = "townhouse"
    APARTMENT  = "apartment"
    TYPE_CHOICES = [
        (VILLA, "Villa"),
        (HOUSE, "House"),
        (TOWNHOUSE, "Townhouse"),
        (APARTMENT, "Apartment"),
    ]

    seller          = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="properties")
    street          = models.CharField(max_length=255)
    city            = models.CharField(max_length=100)
    postal          = models.CharField(max_length=20)
    description     = models.TextField()
    property_type   = models.CharField(max_length=10, choices=TYPE_CHOICES)
    listing_price   = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    listing_date    = models.DateField(auto_now_add=True)
    rooms           = models.PositiveSmallIntegerField()
    bedrooms        = models.PositiveSmallIntegerField()
    bathrooms       = models.PositiveSmallIntegerField()
    square_meters   = models.PositiveIntegerField()

    def thumbnail_url(self):
        """Return the first related image’s URL or an empty string."""
        first = self.images.first()
        return first.image.url if first else ""

    def __str__(self):
        return f"{self.street}, {self.city}"

    # is_sold is calculated in purchase_offer.models to avoid circular import


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image    = models.ImageField(upload_to="properties/")
    order    = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f"Image #{self.order} for {self.property}"