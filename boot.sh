#!/bin/sh
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip

pip install -r requirements/requirements.txt

python3 migrate.py db upgrade

gunicorn -b :5000 --access-logfile - --error-logfile - run:app --daemon
# can also be:
# gunicorn -b :5000 --access-logfile - --error-logfile - run:app
# or
# python run.py