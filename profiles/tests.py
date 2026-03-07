"""
Unit tests for the Profile model in profiles.models.

This module verifies:
- The string representation of Profile
- Correct field values
- Relationship with Django User
"""

import pytest


@pytest.mark.django_db
def test_profile_str(profile):
    """
    Test the string representation of the Profile model.

    The __str__ method should return the username
    of the associated user.
    """
    assert str(profile) == "testuser"


@pytest.mark.django_db
def test_profile_fields(profile, user):
    """
    Test that Profile fields are correctly stored.

    Args:
        profile (Profile): Fixture providing a Profile instance.
        user (User): Fixture providing a User instance.
    """
    assert profile.user == user
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_user_relationship(profile):
    """
    Test the one-to-one relationship between User and Profile.

    Ensures the related_name 'new_user' works correctly.
    """
    assert profile.user.new_user == profile
