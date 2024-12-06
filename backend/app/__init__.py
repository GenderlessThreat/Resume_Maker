from backend.config import Config
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
    CORS(app)
    app.config.from_object(Config)

    # Register blueprints
    from backend.app.routes import resume_bp
    app.register_blueprint(resume_bp, url_prefix='/api')

    return app 
