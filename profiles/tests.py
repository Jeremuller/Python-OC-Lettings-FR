"""
Unit tests for the Profile model in profiles.models.

This module verifies:
- The string representation of Profile
- Correct field values
- Relationship with Django User
"""

import pytest
from django.urls import reverse, resolve
from profiles import views


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


"""
URL tests for the profiles application.

This module verifies that URL patterns defined in profiles.urls
correctly resolve to the expected view functions and that
URL reversing works as intended.
"""


@pytest.mark.django_db
def test_profiles_index_url_reverse():
    """
    Test that the profiles index URL is correctly reversed.

    Ensures the 'profiles:profiles_index' named route
    generates the expected URL path.
    """
    url = reverse("profiles:profiles_index")
    assert url == "/profiles/"


@pytest.mark.django_db
def test_profiles_index_url_resolves():
    """
    Test that the profiles index URL resolves
    to the correct view function.
    """
    resolver = resolve("/profiles/")
    assert resolver.func == views.profiles_index


@pytest.mark.django_db
def test_profile_detail_url_reverse():
    """
    Test that the profile detail URL is correctly reversed.

    Ensures the 'profiles:profile' named route generates
    the expected URL when provided with a username.
    """
    url = reverse("profiles:profile", args=["testuser"])
    assert url == "/profiles/testuser/"


@pytest.mark.django_db
def test_profile_detail_url_resolves():
    """
    Test that the profile detail URL resolves
    to the correct view function.
    """
    resolver = resolve("/profiles/testuser/")
    assert resolver.func == views.profile


"""
View tests for the profiles application.

This module verifies that profile-related views return the correct
HTTP responses, use the expected templates, and provide the correct
context data.
"""


@pytest.mark.django_db
def test_profiles_index_view_status_code(client, profile):
    """
    Test that the profiles index view returns HTTP 200.

    Args:
        client (Client): Django test client.
        profile (Profile): Fixture providing a Profile instance.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_index_view_template(client, profile):
    """
    Test that the profiles index view uses the correct template.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profiles_index_context(client, profile):
    """
    Test that the profiles index view includes profiles in context.
    """
    response = client.get(reverse("profiles:profiles_index"))
    assert "profiles_list" in response.context
    assert profile in response.context["profiles_list"]


@pytest.mark.django_db
def test_profile_detail_view_status_code(client, profile):
    """
    Test that the profile detail view returns HTTP 200
    for an existing profile.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_view_template(client, profile):
    """
    Test that the profile detail view uses the correct template.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert "profiles/profile.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_detail_context(client, profile):
    """
    Test that the profile detail view passes the correct
    profile object to the template context.
    """
    response = client.get(reverse("profiles:profile", args=[profile.user.username]))
    assert "profile" in response.context
    assert response.context["profile"] == profile


@pytest.mark.django_db
def test_profile_detail_nonexistent(client):
    """
    Test that requesting a non-existing profile raises an error.

    Since the view uses Profile.objects.get(), Django will raise
    a Profile.DoesNotExist exception, resulting in a server error.
    """
    with pytest.raises(Exception):
        client.get(reverse("profiles:profile", args=["unknownuser"]))
