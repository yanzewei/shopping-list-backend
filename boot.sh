#!/bin/sh
python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements/requirements.txt

python3 migrate.py db upgrade

gunicorn -b :5003 --access-logfile - --error-logfile - run:app
# can also be:
# gunicorn -b :5000 --access-logfile - --error-logfile - run:app
# or
# python run.py