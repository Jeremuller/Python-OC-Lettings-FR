"""
Database models for the lettings application.

This module defines the core data structures used to represent
rental properties and their associated addresses.

Two main models are provided:

- Address: Represents a physical location with validation constraints.
- Letting: Represents a rental unit associated with a unique address.

These models are mapped to dedicated database tables and enforce
basic validation rules at the model level.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address associated with a letting.

    The Address model stores structured location data and enforces
    validation rules on numerical and string-based fields to ensure
    consistency of stored information.

    Attributes:
        number (PositiveIntegerField): Street number (maximum 4 digits).
        street (CharField): Street name (maximum 64 characters).
        city (CharField): City name (maximum 64 characters).
        state (CharField): Two-character state code (minimum length enforced).
        zip_code (PositiveIntegerField): Postal code (maximum 5 digits).
        country_iso_code (CharField): ISO country code (3 characters minimum).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """
        Return a human-readable representation of the address.

        Returns:
            str: A formatted string combining street number and street name.
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Metadata configuration for the Address model.
        """

        db_table = "lettings_address"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a rental property.

    The Letting model links a rental unit to a unique Address instance
    using a one-to-one relationship. Each letting corresponds to exactly
    one physical address.

    Attributes:
        title (CharField): Name or title of the letting (maximum 256 characters).
        address (OneToOneField): Unique associated Address instance.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human-readable representation of the letting.

        Returns:
            str: The lettings title.
        """
        return self.title

    class Meta:
        """
        Metadata configuration for the Letting model.
        """

        db_table = "lettings_letting"
