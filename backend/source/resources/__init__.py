# -*- coding: utf-8 -*-
import logging

import flask_restful
from flask import Response as FlaskResponse

from errors import api_errors as ApiErrorTypes
from errors.api_errors import ApiError
from repositories.api_repository import ApiRepository
from utils import JSONEncoder

logger = logging.getLogger(__name__)


def exception_handler(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiError as error:
            return Response.error(error)
        except Exception as e:
            logger.error(e, exc_info=True)
            return Response.error(ApiErrorTypes.GENERIC)

    return func_wrapper


class Resource(flask_restful.Resource):
    def __init__(self):
        self.repository = ApiRepository()

    method_decorators = [exception_handler]


class Response:
    @staticmethod
    def success(data, http_code=200):
        return FlaskResponse(JSONEncoder().encode({
            "data": data,
            "error": None
        }), status=http_code, mimetype='application/json')

    @staticmethod
    def error(error):
        return FlaskResponse(JSONEncoder().encode({
            "data": None,
            "error": {
                "message": error.message,
                "code": error.internal_code
            }
        }), status=error.http_code, mimetype='application/json')
