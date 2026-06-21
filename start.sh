#!/bin/sh
set -e

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Loading initial data..."
python manage.py loaddata data.json

echo "Starting Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000}