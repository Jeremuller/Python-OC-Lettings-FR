"""
Models for the profiles application.

This module defines the Profile model, which extends the built-in
Django User model with additional application-specific data,
such as the user's favorite city.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model extending Django's built-in User.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model,
            ensuring each user has a single profile. The related_name
            "new_user" allows reverse access from User instances.
        favorite_city (CharField): Optional field storing the user's
            favorite city, with a maximum length of 64 characters.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="new_user")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the Profile instance.

        Returns:
            str: The username of the associated User.
        """
        return self.user.username

    class Meta:
        """
        Metadata for the Profile model.

        Attributes:
            db_table (str): Explicit database table name for the model.
        """
        db_table = "profiles_profile"
