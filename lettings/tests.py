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


"""
URL tests for the lettings application.

This module verifies that URL patterns defined in lettings.urls
correctly resolve to their associated view functions and that
named routes generate the expected paths.

The following aspects are tested:
- URL reversing using Django's reverse function
- URL resolution using Django's resolve function
- HTTP response status codes for defined routes
"""

import pytest
from django.urls import reverse, resolve
from lettings import views


@pytest.mark.django_db
def test_lettings_index_url_reverse():
    """
    Test that the lettings index URL is correctly reversed.

    Ensures that the named route 'lettings:lettings_index'
    generates the expected URL path.
    """
    url = reverse("lettings:lettings_index")
    assert url == "/lettings/"


@pytest.mark.django_db
def test_letting_detail_url_reverse(letting):
    """
    Test that the letting detail URL is correctly reversed
    with a valid letting ID.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    url = reverse("lettings:letting", args=[letting.id])
    assert url == f"/lettings/{letting.id}/"


@pytest.mark.django_db
def test_lettings_index_url_resolves():
    """
    Test that the lettings index URL resolves
    to the correct view function.
    """
    resolver = resolve("/lettings/")
    assert resolver.func == views.lettings_index


@pytest.mark.django_db
def test_letting_detail_url_resolves(letting):
    """
    Test that the letting detail URL resolves
    to the correct view function.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    resolver = resolve(f"/lettings/{letting.id}/")
    assert resolver.func == views.letting


@pytest.mark.django_db
def test_lettings_index_http_response(client):
    """
    Integration test ensuring that the lettings index
    URL returns an HTTP 200 response.
    """
    response = client.get(reverse("lettings:lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_http_response(client, letting):
    """
    Integration test ensuring that the letting detail
    URL returns an HTTP 200 response for a valid ID.

    Args:
        letting (Letting): Fixture providing a sample Letting instance.
    """
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200
