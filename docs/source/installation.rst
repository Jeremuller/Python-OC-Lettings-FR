Installation
============

This section explains how to install and configure the Orange County Lettings project in a local environment.

Unlike the README, which focuses on quick usage, this section provides a more detailed explanation of the setup process and execution environments.

The project supports two installation modes:

- Local Python environment (development)
- Docker-based environment (production-like)

Prerequisites
-------------

Before installing the project, ensure the following tools are available:

- Git
- Python 3.10+
- pip
- Docker and Docker Compose (optional but recommended)


Project cloning
---------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR


Local development setup
-----------------------

This setup is intended for development without containers.

Virtual environment
~~~~~~~~~~~~~~~~~~~

A virtual environment isolates the project's Python dependencies from the global interpreter.

Create a virtual environment:

.. code-block:: bash

   python -m venv venv

Activate it:

.. code-block:: bash

   # Linux / macOS
   source venv/bin/activate

   # Windows
   venv\Scripts\activate

Dependency installation
~~~~~~~~~~~~~~~~~~~~~~~

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

This installs Django together with the libraries required for testing, code quality checks and production deployment.

Environment configuration
-------------------------

The application relies on environment variables.

Create a `.env` file at the root of the project.

Required variables:

- SECRET_KEY
- DEBUG
- USE_SQLITE
- SENTRY_DSN (optional)

For PostgreSQL environments:

- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT


Database setup
--------------

Apply migrations before running the application:

.. code-block:: bash

   python manage.py migrate


Run development server
----------------------

.. code-block:: bash

   python manage.py runserver

Access:

http://localhost:8000


Docker setup
-------------

The project also provides a Docker Compose configuration allowing the entire application stack to be started with a single command.

This setup is recommended for:

- production-like execution
- reproducibility
- avoiding local dependency issues

Start containers:

.. code-block:: bash

   docker compose up --build


Container initialization
------------------------

On startup, the container automatically:

- applies database migrations
- starts the Gunicorn server

This is handled by the `start.sh` script.

This guarantees that the database schema is always synchronized before the application starts serving requests.


Environment differences
-----------------------

- Local setup → SQLite (simpler, development-friendly)
- Docker setup → PostgreSQL (production-like)


Summary
-------

Two execution modes are available:

- Local environment → development and debugging
- Docker environment → production-like behavior