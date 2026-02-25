"""
URL configuration for the lettings application.

This module defines the URL patterns associated with the lettings app.
It maps URL paths to their corresponding view functions responsible
for rendering letting listings and individual letting details.

The `app_name` variable enables namespaced URL resolution within
the Django project.
"""

from django.urls import path

from . import views

app_name = "lettings"
urlpatterns = [
    # Root path: displays the list of all available lettings
    path("", views.lettings_index, name="lettings_index"),

    # Dynamic route: displays details for a specific letting
    # identified by its primary key (letting_id)
    path("<int:letting_id>/", views.letting, name="letting"),
]
