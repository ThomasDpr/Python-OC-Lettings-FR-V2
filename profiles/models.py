"""
Models module for the profiles application.

This module defines the database models for managing user profiles,
extending the built-in Django User model with additional fields.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    This model extends the Django User model with additional profile
    information such as the user's favorite city.

    Attributes:
        user: One-to-one relationship to the Django User model.
        favorite_city: The user's favorite city (optional, max 64 characters).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="oc_profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a string representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
