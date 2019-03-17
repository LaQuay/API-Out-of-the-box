# -*- coding: utf-8 -*-
import logging

from api import create_app
from resources.resources_loader import Resources

logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    Resources.init_cors(app)
    app.run(debug=True, host='0.0.0.0')
