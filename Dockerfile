# pulling image from docker hub
FROM python:3.8.3-alpine

# set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN addgroup -S admin && adduser -S -G admin admin
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir $APP_HOME/src

WORKDIR $APP_HOME

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./src .
# COPY .env.dev .env


RUN chgrp -R admin $APP_HOME
RUN chown -R admin:admin $APP_HOME
RUN chmod -R 760 $APP_HOME

USER admin



