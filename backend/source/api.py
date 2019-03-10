import logging

from flask import Flask
from flask_restful import Api

from resources.resources_loader import Resources
from utils import db_uri

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    logger.info("Connecting to the DB")

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ERROR_404_HELP'] = False

    with app.app_context():
        from core import database
        database.init_db()
        # TODO Future improvement
        # yield app

    Resources.load_resources(api)

    return app
