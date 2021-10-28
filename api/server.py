import os

if os.environ.get('FLASK_ENVIRONMENT','localhost') == 'localhost':
    from dotenv import load_dotenv
    # take environment variables from .env.
    load_dotenv()

#from config import Config
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask("datapilot")
    CORS(app)
    app.config.from_pyfile(os.path.join(os.path.dirname(__file__),"config.py"))
    db = SQLAlchemy(app)
    db.init_app(app)
    return app, db

app,db = create_app()
api = Api(app)

from resources.helloworld import HelloWorld
from resources.setup import Setup
api.add_resource(HelloWorld, '/hello')
api.add_resource(Setup, '/setup')

if __name__ == '__main__':
    app.run(debug=True, port=1235)