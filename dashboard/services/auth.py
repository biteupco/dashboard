# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import logging
import json

import requests

from dashboard.libs.exceptions import HTTPBadRequest
from dashboard import constants


logger = logging.getLogger(__name__)


class AuthLoginException(HTTPBadRequest):
    """Subclass to HTTPBadRequest class so that app handles this exception as-if it is HTTPBadRequest"""
    pass


class AuthService():
    """AuthService (wrapper) to perform authentication services with the Auth Service endpoint (bouncer)

    Borg Singleton pattern
    """
    __state = {}

    @classmethod
    def set_env(cls, env):
        cls.env = env

    def _get_base_url(self):
        return constants.AUTH_SERVICE_URL_MAP.get(self.__class__.env)  # based on env settings

    def __init__(self):
        self.__dict__ = self.__state

        if 'base_url' not in self.__dict__:
            # init instance
            self.base_url = self._get_base_url()
            self.url_map = {
                constants.AUTH_BASIC: 'auth/login/basic',
                constants.AUTH_FACEBOOK: 'auth/login/facebook'
            }

    def _send_requests(self, url, method='get', params=None, payload=None):
        try:
            url = '/'.join([self.base_url, url])  # concatenate URL
            headers = {'Content-type': 'application/json'}
            resp = requests.request(method, url, headers=headers, params=params, data=json.dumps(payload))

            if resp.status_code >= 400:  # error occured
                logger.exception(resp.text)
                raise Exception(resp.text)

            return resp.json() or resp.text  # return json body of response

        except Exception as e:
            logger.exception(e.message)
            raise AuthLoginException()

    def _login(self, payload, provider):
        """Base method to login/signup with AuthService, returning a valid SSO token and user_id if successful"""
        json_resp = self._send_requests(self.url_map[provider], method='post', payload=payload)
        token = json_resp.get('token')
        user_id = json_resp.get('user_id')
        if not token:
            err_msg = 'token not found in response'
            logger.exception(err_msg)
            raise Exception(err_msg)

        return token, user_id

    def login(self, payload, provider=constants.AUTH_BASIC):
        """Login method to authenticate against AuthService, returning token if successful"""

        # supported login methods
        supported_login_methods = [constants.AUTH_BASIC]

        if provider not in supported_login_methods:
            err_msg = '{} login is currently not supported.'.format(provider)
            logger.exception(err_msg)
            raise Exception(err_msg)

        return self._login(payload, provider)

    def signup(self, payload, provider=constants.AUTH_BASIC):
        """Signup method to register new user with AuthService; returning token if successful"""

        # supported signup methods
        supported_login_methods = [constants.AUTH_BASIC]

        if provider not in supported_login_methods:
            err_msg = '{} login is currently not supported.'.format(provider)
            logger.exception(err_msg)
            raise Exception(err_msg)

        return self._login(payload, provider)
