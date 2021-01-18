from flask import Flask

def create_app(environment="development"):
    app = Flask(__name__)
    

    return app