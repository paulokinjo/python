FROM python:3.10-slim as common-base

ENV DJANGO_SETTINGS_MODULE superlists.settings

FROM common-base as builder

RUN pip install -u pip setuptools

RUN mkdir -p /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essentials python3-dev
RUN mkdir -p /install

COPY requirements.txt /install

RUN sh -c 'pip install --no-warn-script-location --prefix=/install .'