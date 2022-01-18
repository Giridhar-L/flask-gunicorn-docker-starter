from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from app.config import Config

cors=CORS()
def create_app():
    app = Flask(__name__)
    
    # set logger
    logger = logging.getLogger('gunicorn.error')
    logger.setLevel(logging.INFO)
    app.logger = logger

    # Printing test env vars
    app.logger.info(Config.TEST_ENV_VAR1)
    app.logger.info(Config.TEST_ENV_VAR2)

    # init cors
    cors.init_app(app)
    
    with app.app_context():
        from app.routes import app_routes
        return app

app = create_app() 

