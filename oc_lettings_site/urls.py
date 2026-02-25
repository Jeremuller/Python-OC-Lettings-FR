"""
URL configuration for the main Django project (oc_lettings_site).

This module defines the root URL patterns for the project, including:

- The home page (`index`)
- Inclusion of the lettings app URLs
- Inclusion of the profiles app URLs
- Django admin interface

It maps URL paths to the corresponding view functions or included
URLconfs. Namespacing is managed at the app level where necessary.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Lettings app: routes are defined in lettings.urls
    path('lettings/', include('lettings.urls')),

    # Profiles app: routes are defined in profiles.urls
    path('profiles/', include('profiles.urls')),

    # Django admin interface
    path('admin/', admin.site.urls),
]
