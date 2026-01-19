"""
Models module for the lettings application.

This module defines the database models for managing property lettings,
including the Address and Letting models.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing a physical address for a letting property.

    This model stores all components of a US-style postal address,
    including street number, street name, city, state, ZIP code,
    and country ISO code.

    Attributes:
        number: The street number (1-9999).
        street: The street name (max 64 characters).
        city: The city name (max 64 characters).
        state: The two-letter state abbreviation.
        zip_code: The ZIP code (1-99999).
        country_iso_code: The three-letter ISO country code.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Meta options for the Address model."""

        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Return a string representation of the address.

        Returns:
            str: The street number and street name combined.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Model representing a property letting.

    This model links a letting title to a specific address,
    representing a property available for rent.

    Attributes:
        title: The title or name of the letting (max 256 characters).
        address: One-to-one relationship to an Address instance.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
