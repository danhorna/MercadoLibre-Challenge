from flask import Flask
from flask_restful import Api
from app.resources.api import SearchInDoc

def create_app(environment="development"):
    app = Flask(__name__)

    #api
    api = Api(app)

    api.add_resource(SearchInDoc, '/search-in-doc/<id>')

    return app