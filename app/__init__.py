from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from config import Config
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the database
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints/routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
