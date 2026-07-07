Technologies
============

The Orange County Lettings project is built on a modern Python web stack designed for scalability, maintainability, and deployment readiness.

Backend
-------

- Python 3.10: main programming language
- Django 3.0: web framework used for application structure, routing, and ORM

Databases
----------

- SQLite: used for CI unit tests and fast setup
- PostgreSQL: used in Docker and production environments

Containerization
-----------------

- Docker: container runtime for the application
- Docker Compose: orchestration of multi-service environments

CI/CD
-----

- GitHub Actions: automated workflows for testing, linting, and deployment

Testing and code quality
------------------------

- pytest / pytest-django: unit and integration testing
- coverage: test coverage measurement
- flake8: linting for code style and quality
- black: code formatting

Production stack
----------------

- Gunicorn: WSGI HTTP server for running Django in production
- WhiteNoise: static file serving without external storage
- Render: cloud platform used for deployment

Monitoring and configuration
-----------------------------

- Sentry: error tracking and monitoring
- python-dotenv: environment variable management via `.env` files