import logging

from flask import Flask
from flask_restful import Api

from core import database
from core.database import db_uri
from repositories.api_repository import ApiRepository
from resources.resources_loader import Resources

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    logger.info("Connecting to DB")

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ERROR_404_HELP'] = False

    with app.app_context():
        database.init_db()
        # TODO Future improvement
        # yield app

    Resources.load_resources(api)

    return app
