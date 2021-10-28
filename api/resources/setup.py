from models import Configuration,Dictionary,Migratons
from flask_restful import Resource
from server import db

class Setup(Resource):
    def get(self):
        db.create_all()
        return {'message':'database is created'}, 200
