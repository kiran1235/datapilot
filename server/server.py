from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.helloworld import HelloWorld

app = Flask("datapilot")
CORS(app)

api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=1235)