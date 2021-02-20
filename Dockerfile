# pulling image from docker hub
FROM python:3.8.3-alpine

# set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN addgroup -S admin && adduser -S -G admin admin
ENV HOME=/usr/src
ENV APP_HOME=/usr/src/app
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles

WORKDIR $APP_HOME

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app .
# COPY .env.dev .env


RUN chgrp -R admin $APP_HOME
RUN chown -R admin:admin $APP_HOME
RUN chmod -R 760 $APP_HOME

USER admin



