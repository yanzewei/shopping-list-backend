# FLASK

## File Structure

### migrations

The version control of MySQL via Flask Migration.

### services

Provide the restful API.

### models.py

Mysql ORM

### redismodels.py

Flask redis

### run.py

Entry file. Can execute `python run.py` to run the application after building up the environment.

### migrate.py

Use it to control the migrations.
Can type `python migrate.py db --help` to check the detail.

### boot.sh

The script used to build up the environment.
