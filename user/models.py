from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user with an optional profile image."""
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return self.get_full_name() or self.username