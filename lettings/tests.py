# tests/test_models.py
"""
Unit tests for the lettings.models module.

This file contains tests for the Address and Letting models,
ensuring that model fields, string representations, and
basic validations work correctly.

Fixtures:
    - address: Pre-created Address instance for tests.
"""

import pytest
from lettings.models import Address


@pytest.mark.django_db
def test_address_str(address):
    """
    Test the string representation of the Address model.

    The __str__ method should return a formatted string combining
    the street number and the street name.

    Args:
        address (Address): Fixture providing a sample Address instance.
    """
    assert str(address) == "123 Main Street"


@pytest.mark.django_db
def test_address_fields(address):
    """
    Test that the Address fields are correctly set from the fixture.

    Args:
        address (Address): Fixture providing a sample Address instance.
    """
    assert address.number == 123
    assert address.street == "Main Street"
    assert address.city == "Los Angeles"
    assert address.state == "CA"
    assert address.zip_code == 90001
    assert address.country_iso_code == "USA"


# tests/test_models.py
"""
Unit tests for the Letting model in lettings.models.

This file contains tests for the Address and Letting models,
ensuring that model fields, string representations, and
one-to-one relationships work correctly.
"""

import pytest
from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_str(letting):
    """
    Test the string representation of the Letting model.

    The __str__ method should return the title of the letting.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    assert str(letting) == "Beautiful Apartment"


@pytest.mark.django_db
def test_letting_fields(letting, address):
    """
    Test that the Letting fields are correctly set and linked to Address.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
        address (Address): Fixture providing a sample Address instance.
    """
    assert letting.title == "Beautiful Apartment"
    # Check the one-to-one relationship
    assert letting.address == address
    # Confirm related data
    assert letting.address.street == "Main Street"
    assert letting.address.city == "Los Angeles"
