"""
Views for the main Django project (oc_lettings_site).

This module contains view functions responsible for rendering
the templates of the project's main pages, such as the home page.
"""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the home page of the Orange County Lettings site.

    This view handles requests to the root URL ('/') and returns
    the main landing page.

    An info log is recorded to track normal application traffic.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered home page template.
    :rtype: HttpResponse
    """
    logger.info("Homepage accessed")

    return render(request, "index.html")


def page_not_found(request, exception):
    """
    Render the custom 404 error page.

    This view is used by Django when a requested URL does not exist.

    A warning log is recorded to track invalid navigation attempts.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param exception: The exception raised by the resolver.
    :type exception: Exception
    :return: Rendered 404 error page with HTTP status 404.
    :rtype: HttpResponse
    """
    logger.warning("404 error encountered", extra={"path": request.path, "method": request.method})
    return render(request, "404.html", status=404)


def server_error(request):
    """
    Render the custom 500 error page.

    This view is used by Django when an unhandled server error occurs.

    An error log is recorded to capture critical failures for
    monitoring and debugging purposes.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered 500 error page with HTTP status 500.
    :rtype: HttpResponse
    """
    logger.error("500 error encountered", extra={"path": request.path, "method": request.method})
    return render(request, "500.html", status=500)
