Introduction
============

Project overview
----------------

Orange County Lettings is a web application built with the Django framework.

The application allows users to browse property listings and view detailed information about associated profiles.

The project follows a modular architecture in order to clearly separate concerns between the different application components (users, listings, main site, etc.).

Development context
-------------------

This project was developed as part of the **Python Application Developer** training program provided by OpenClassrooms.

It serves as a practical implementation of key software engineering concepts, including:

- web application development using Django
- modular project architecture design
- reproducible development environments
- continuous integration and deployment (CI/CD)
- production deployment automation

Technical objectives
--------------------

Beyond functional implementation, this project aims to demonstrate the ability to manage a complete software development lifecycle:

- source code management with Git and GitHub
- code quality enforcement using linting (flake8)
- unit testing with pytest
- test coverage measurement
- automated checks using GitHub Actions
- containerization with Docker
- automated deployment to production environments

High-level architecture
-----------------------

The application is composed of several main components:

- a Django web application handling business logic and user interface
- a relational database system, using SQLite in development/testing and PostgreSQL in production
- a CI/CD pipeline responsible for automated testing and deployment
- a containerized deployment infrastructure using Docker and Render

The following sections of this documentation provide details on installation, usage, system architecture, and deployment procedures.