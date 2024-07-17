#!/bin/sh
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn Django_Gunicorn.wsgi:application --bind 0.0.0.0:13579