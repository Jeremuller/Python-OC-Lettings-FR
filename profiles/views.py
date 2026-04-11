"""
Views module for the profiles application.

This module contains the view functions responsible for rendering
the profiles list and individual profile detail pages.
Each view retrieves data from the database and passes it to
the corresponding templates for rendering.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile

import logging

logger = logging.getLogger(__name__)


def profiles_index(request):
    """
    Render a page displaying all profiles.

    Retrieves all Profile instances from the database and passes them
    to the 'profiles/index.html' template under the context variable
    'profiles_list'.

    This view logs access events for monitoring purposes.

    :param request: The HTTP request object.
    :type request: HttpRequest

    :return: Rendered HTML page with the list of profiles.
    :rtype: HttpResponse
    """

    logger.info(
        "Profiles list accessed",
        extra={
            "path": request.path,
            "method": request.method,
        },
    )
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Render a page displaying details of a specific profile.

    Retrieves a Profile instance from the database corresponding
    to the provided username and passes it to the
    'profiles/profile.html' template under the context variable 'profile'.

    This view logs access events for monitoring purposes.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param username: The username of the user whose profile is requested.
    :type username: str

    :return: Rendered HTML page with the profile details.
    :rtype: HttpResponse

    :raises Http404: If no profile matches the given username.
    """

    logger.info(
        "Profile detail accessed",
        extra={
            "username": username,
            "path": request.path,
            "method": request.method,
        },
    )
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
