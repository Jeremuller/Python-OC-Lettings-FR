"""
URL configuration for the profiles application.

This module defines the URL patterns associated with the profiles app.
It maps URL paths to their corresponding view functions responsible
for rendering profile listings and individual profile details.

The `app_name` variable enables namespaced URL resolution within
the Django project.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    # Root path: displays the list of all available profiles
    path("", views.profiles_index, name="profiles_index"),

    # Dynamic route: displays details for a specific profile
    # identified by the username
    path("<str:username>/", views.profile, name="profile"),
]
