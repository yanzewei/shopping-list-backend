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

Enter the root directory. source boot.sh

Create the file named .env under the root directory. Because the environment variables of deployment and production are different, moreover,

the production's database information is private, this file is ignored in git.

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

The nginx.config can be used.
