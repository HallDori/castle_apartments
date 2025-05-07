from django.db import models

class Seller(models.Model):
    AGENCY     = "agency"
    INDIVIDUAL = "individual"
    TYPE_CHOICES = [
        (AGENCY, "Real Estate Agency"),
        (INDIVIDUAL, "Individual"),
    ]

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