FROM python:3.6-alpine

ENV FLASK_APP run.py

RUN adduser -D flask
USER flask

WORKDIR /home/shopping-list-backend

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY routes routes
COPY services services
COPY migrations migrations
COPY *.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
