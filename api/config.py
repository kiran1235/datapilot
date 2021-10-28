import os

# class Config(object):
"""Set Flask configuration vars from .env file."""

# General
TESTING = os.environ["FLASK_ENVIRONMENT"]
FLASK_DEBUG = os.environ["FLASK_DEBUG"]
ENV = os.environ['ENV']
# Database
SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
SQLALCHEMY_ECHO = True if os.environ["SQLALCHEMY_ECHO"] == 'true' else False
SQLALCHEMY_TRACK_MODIFICATIONS = True if os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"] == 'true' else False

