"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Blob client (accessible via app.config)
# blob_connection_string = f"DefaultEndpointsProtocol=https;AccountName={app.config['BLOB_ACCOUNT_NAME']};AccountKey={app.config['BLOB_ACCOUNT_KEY']};EndpointSuffix=core.windows.net"
# app.blob_service = BlobServiceClient.from_connection_string(blob_connection_string)

 # Logging configuré pour App Service
if not app.debug:
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_error_logger.handlers
    app.logger.setLevel(logging.INFO)

# Pour forcer les logs sur stdout (Azure les lit ici)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
stream_handler.setFormatter(formatter)
app.logger.addHandler(stream_handler)

import FlaskWebProject.views
