#!/bin/sh
python -m venv venv

source venv/bin/activate

pip install -r requirements/requirements.txt

python migrate.py db upgrade

gunicorn -b :5000 --access-logfile - --error-logfile - run:app --daemon
# can also be:
# gunicorn -b :5000 --access-logfile - --error-logfile - run:app
# or
# python run.py
