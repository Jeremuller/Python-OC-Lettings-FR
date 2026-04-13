"""
Views for the lettings application.

This module defines view functions responsible for displaying
the list of available lettings and the details of a specific letting.

Each view retrieves data from the database using the Letting model
and renders the appropriate HTML template with a context dictionary.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Letting

import logging

logger = logging.getLogger(__name__)


def lettings_index(request: HttpRequest) -> HttpResponse:
    """
    Display the list of all available lettings.

    This view retrieves all Letting instances from the database
    and renders them using the ``lettings/index.html`` template.

    This view logs access attempts for monitoring purposes.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered HTML page displaying the list of lettings.
    :rtype: HttpResponse
    """
    logger.info(
        "Lettings list accessed",
        extra={
            "path": request.path,
            "method": request.method,
        },
    )
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Display the details of a specific letting.

    This view retrieves a single Letting instance based on its
    primary key and renders its details using the
    ``lettings/letting.html`` template.

    This view logs access attempts for monitoring purposes.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param letting_id: The unique identifier of the letting.
    :type letting_id: int
    :return: Rendered HTML page displaying the letting details.
    :rtype: HttpResponse
    :raises Http404: If no letting matches the given ID.
    """
    logger.info(
        "Letting detail accessed",
        extra={
            "letting_id": letting_id,
            "path": request.path,
            "method": request.method,
        },
    )
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
