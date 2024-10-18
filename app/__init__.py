from flask import Flask
from .views import app as api_views

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_views, url_prefix='/api')  # Register the blueprint
    return app
