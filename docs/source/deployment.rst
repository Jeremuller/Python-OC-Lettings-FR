Deployment
==========

Deployment overview
-------------------

The application is deployed through an automated CI/CD pipeline.
The deployment process ensures that code quality checks and tests are
validated before releasing a new version.

Continuous integration
----------------------

The CI pipeline is managed with GitHub Actions.

The workflow performs:

- dependency installation;
- code quality checks with flake8;
- automated tests with pytest;
- coverage measurement.

Containerization
----------------

The application is containerized using Docker.

The production container includes:

- the Django application;
- Gunicorn as the WSGI server;
- PostgreSQL database connectivity.

Production environment
----------------------

The application is deployed on Render.

The production environment relies on:

- PostgreSQL for persistent data storage;
- Gunicorn to serve the Django application;
- WhiteNoise for static files handling.

Monitoring
----------

Application monitoring is provided through Sentry, which collects runtime
errors and helps identify production issues.