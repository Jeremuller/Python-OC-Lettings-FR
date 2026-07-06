Architecture
============

Orange County Lettings is organized as a modular Django project. Each application
is responsible for a specific functional domain, which improves maintainability
and simplifies future developments.

Project structure
-----------------

The project is composed of three main Django applications:

- ``oc_lettings_site``: global project configuration (settings, URL routing, WSGI application and shared resources);
- ``lettings``: management of property listings;
- ``profiles``: management of user profiles.

This separation follows Django's recommended application architecture and keeps
business logic isolated from project configuration.

Source code documentation
-------------------------

The following sections are automatically generated from the project's docstrings
using the Sphinx ``autodoc`` extension.

They provide detailed information about the available modules, classes,
functions and views without duplicating the source code documentation.

.. toctree::
   :maxdepth: 2

   architecture/oc_lettings_site
   architecture/lettings
   architecture/profiles