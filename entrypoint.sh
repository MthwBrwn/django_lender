#!/bin/bash

set -e

cd /src

coverage run --source='.' manage.py test -v 2 && \
python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000
