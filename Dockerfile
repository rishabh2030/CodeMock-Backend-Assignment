FROM python:3.11.7-slim-bullseye

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

RUN apt-get update

COPY ./requirements.txt . 

RUN pip install -r requirements.txt