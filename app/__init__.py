from flask import Flask
from flask_restful import Api
from app.resources.api import SearchInDoc, NewFile

def create_app():
    app = Flask(__name__)

    #api
    api = Api(app)

    api.add_resource(SearchInDoc, '/search-in-doc/<id>')
    api.add_resource(NewFile, '/file')

    return app