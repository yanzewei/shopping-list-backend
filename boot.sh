#!/bin/sh
source venv/bin/activate

python migrate.py db upgrade

exec gunicorn -b :5000 --access-logfile - --error-logfile - run:app
