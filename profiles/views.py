"""
Views module for the profiles application.

This module contains the view functions responsible for rendering
the profiles list and individual profile detail pages.
Each view retrieves data from the database and passes it to
the corresponding templates for rendering.
"""

from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Render a page displaying all profiles.

    Retrieves all Profile instances from the database and passes them
    to the 'profiles/index.html' template under the context variable
    'profiles_list'.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render a page displaying details of a specific profile.

    Retrieves a Profile instance from the database corresponding
    to the provided username and passes it to the
    'profiles/profile.html' template under the context variable 'profile'.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is requested.

    Returns:
        HttpResponse: Rendered HTML page with the profile details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
