#!/usr/bin/env bash
#exit on error

set -o errexit

pip install -r requerimientos.txt
python manage.py collections --no-input
python manage.py migrate 