# -*- coding: utf-8 -*-
from flask_cors import CORS

from resources.api_handlers import EntryHandler


class Resources:
    def init_cors(app):
        # CORS(app, resources=r'/entries/*', origins=cors_origins)
        pass

    @staticmethod
    def load_resources(api):
        api.add_resource(EntryHandler.Entries, '/entries/',
                         strict_slashes=False)

        api.add_resource(EntryHandler.Entry, '/entries/<string:entry_id>',
                         strict_slashes=False)
