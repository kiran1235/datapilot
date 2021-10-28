FROM python:3.9.7-slim-buster as base
# Base image to be reused
LABEL maintainer "Kiran Kumar Talapaku <kiran.talapaku@gmail.com>"
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
ENV FLASK_APP=server.py
EXPOSE 1235

FROM base as debug
# Debug image reusing the base
# Install dev dependencies for debugging
RUN pip install debugpy
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

FROM base as prod
# Production image
RUN pip install gunicorn
COPY . .
CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:1235", "wsgi:app"]