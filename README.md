# shopping-list-backend

## Contents

- [Requirements](#-requirements)
- [Documentation](#-documentation)
- [Building And Deployment](#-building-and-deployment)

## 📋 Requirements

shopping-list-backend requires python3, pip3, python-dev.

## 📖 Documentation

The restful api documentation can see the [restful api](https://github.com/yanzewei/shopping-list-backend/blob/master/documents/RESTFUL_API.md)

The database design document can see the [database design](https://github.com/yanzewei/shopping-list-backend/blob/master/documents/DATABASE_DESIGN.md)

The falsk related document can see the [flask](https://github.com/yanzewei/shopping-list-backend/blob/master/documents/FLASK.md)

## 🎉 Building And Deployment

Create the file named **.env** under the root directory. Because the environment variables of deployment and production are different, moreover,

the production's database information is private, this file should be ignored in git.

The format should be like this:

### Local
```
FLASK_CONFIG=development
DEV_MYSQL_URL="mysql://username:password@localhost/dbname"
DEV_REDIS_URL="redis://localhost:6379/0"
```

### Production
```
FLASK_CONFIG=production
MYSQL_URL="mysql://username:password@localhost/dbname"
REDIS_URL="redis://:password@localhost:6379/0"
```


Enter the root directory. Run the command: `source boot.sh`

You can modify the boot.sh according to your practical needs. Like change the port or run it without gunicorn.
```
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
```

The nginx.config can be used to depoy in linux. But the docker configure is incomplete, so do not use it.
