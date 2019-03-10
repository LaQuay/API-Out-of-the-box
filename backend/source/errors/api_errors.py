# -*- coding: utf-8 -*-
"""
Custom errors factory.
"""


class ApiError(Exception):
    def __init__(self, message, http_code, internal_code, params=()):
        self.message = message.format(*params)
        self.http_code = http_code
        self.internal_code = internal_code
        super(Exception, self).__init__(self.message)


GENERIC = ApiError("An unexpected error has occurred.", 500, 0)
FIELD_NOT_VALID = ApiError("Field is not valid.", 500, 4)
INVALID_ID = ApiError("Invalid id format.", 404, 1)
EXISTS_ID = ApiError("Id does exists.", 400, 2)
NOT_EXISTS_ID = ApiError("Id does not exists.", 404, 3)
