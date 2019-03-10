# -*- coding: utf-8 -*-
import logging

from api import create_app

logger = logging.getLogger(__name__)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
