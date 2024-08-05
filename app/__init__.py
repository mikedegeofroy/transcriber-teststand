from flask import Flask
from flasgger import Swagger
from .routes import transcribe, generate

def create_app():
    app = Flask(__name__)

    app.register_blueprint(transcribe, url_prefix='/transcribe')
    app.register_blueprint(generate, url_prefix='/avatar')

    swagger = Swagger(app)

    return app
