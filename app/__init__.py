import os
import logging
from flask import Flask
from config import Config
from logging.handlers import TimedRotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Khởi tạo ứng dụng Flask
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config.from_object(Config)

# Khởi tạo SQLAlchemy và Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app.models import * # Import models để chúng có thể được phát hiện bởi Flask-Migrate
print("[DEBUG] Loaded models:", db.metadata.tables.keys())

from app.routes.api import api_bp
app.register_blueprint(api_bp)


# Configures the logging
def configure_logging(app):
    # Create a file handler which logs even debug messages
    handler = TimedRotatingFileHandler('flask-template.log', when='midnight', interval=1, backupCount=10)
    handler.setLevel(logging.INFO)  # Set the log level you want here
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logging(app)

