#!/bin/sh

python manage.py makemigrations
python manage.py migrate

exec gunicorn -w 3 -b 0.0.0.0:8000 stevebrownlee.wsgi
