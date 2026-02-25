"""
Views for the main Django project (oc_lettings_site).

This module contains view functions responsible for rendering
the templates of the project's main pages, such as the home page.
"""

from django.shortcuts import render


def index(request):
    """
    Render the home page of the Orange County Lettings site.

    This view function handles requests to the root URL ('/').
    It returns a response using the 'index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, "index.html")
