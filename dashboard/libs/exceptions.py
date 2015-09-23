# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import


class BaseException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        super(BaseException, self).__init__(self)
        self.message = message
        self.status_code = status_code if status_code else BaseException.status_code
        self.payload = payload

    def __str__(self):
        return "[{}]\nStatus: {}\nError: {}\nPayload: {}\n".format(
            self.__class__.__name__, self.status_code, self.message, self.payload
        )

    def to_dict(self):
        return {
            key: getattr(self, key, default='')
            for key in ['message', 'status_code', 'payload']
        }


class HTTPBadRequest(BaseException):
    status_code = 400
    message = "Invalid request."

    def __init__(self, payload=None):
        BaseException.__init__(self, HTTPInvalidMethod.message, status_code=HTTPInvalidMethod.status_code, payload=payload)


class HTTPUnauthorized(BaseException):
    status_code = 401
    message = "You are not authorized to view this resource."

    def __init__(self, payload=None):
        BaseException.__init__(self, HTTPUnauthorized.message, status_code=HTTPUnauthorized.status_code, payload=payload)


class HTTPInvalidMethod(BaseException):
    status_code = 405
    message = "This method is not allowed."

    def __init__(self, payload=None):
        BaseException.__init__(self, HTTPInvalidMethod.message, status_code=HTTPInvalidMethod.status_code, payload=None)