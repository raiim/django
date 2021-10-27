FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /
RUN apt-get update
RUN apt-get install -y cron
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt