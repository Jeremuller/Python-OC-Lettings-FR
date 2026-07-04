Local Usage
===========

This section describes the different ways to run the application in a local environment once it has been installed.

It includes both a simple Python-based execution and a Docker Compose execution.

---

Running locally with Django
-------------------------------

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

Access the application at:

http://localhost:8000

Running with Docker Compose
------------------------

The project provides a Docker Compose configuration intended to reproduce an
environment close to production.

Before using this execution mode, ensure that:

- Docker is installed and running on the host machine;
- Docker Compose is available;
- a valid ``.env`` file has been created at the root of the project.

The ``docker compose up --build`` command performs several operations:

- builds the application image from the project's Dockerfile;
- creates a dedicated Docker network;
- starts a PostgreSQL container;
- starts the Django application container;
- automatically executes the ``start.sh`` initialization script.

.. code-block:: bash

   docker compose up --build

During startup, the application container automatically applies the database
migrations before launching the Gunicorn server.

Once both containers are running, the application is available at:

::

   http://localhost:8000

---

Both execution modes rely on the same application codebase.

The Django development server is generally preferred during development because it provides automatic code reloading, whereas Docker Compose offers an environment closer to production.