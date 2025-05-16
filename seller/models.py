from django.db import models
from django.conf import settings

class Seller(models.Model):
    AGENCY     = "agency"
    INDIVIDUAL = "individual"
    TYPE_CHOICES = [
        (AGENCY, "Real Estate Agency"),
        (INDIVIDUAL, "Individual"),
    ]
    #assign a seller to a user so you can accept a purchase offer
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="seller_profile",
        null=True,  # for old sellers that were not assigned as users
        blank=True,
    )

    name            = models.CharField(max_length=255)
    kind            = models.CharField(max_length=12, choices=TYPE_CHOICES)
    logo            = models.ImageField(upload_to="sellers/logos/", blank=True, null=True)
    cover           = models.ImageField(upload_to="sellers/covers/", blank=True, null=True)
    bio             = models.TextField(blank=True)
    address_street  = models.CharField(max_length=255, blank=True)
    address_city    = models.CharField(max_length=100,  blank=True)
    address_postal  = models.CharField(max_length=20,   blank=True)

    def __str__(self):
        return self.name