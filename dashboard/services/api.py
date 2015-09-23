# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import logging
import json
from string import Formatter
import requests
from dashboard import constants

logger = logging.getLogger(__name__)


class APIException(Exception):
    pass

API_MAP = {
    # This is a map of method names to their corresponding API endpoints with the backend (HTTPS)
    # method names are almost CRUD-speak (since our backend API tries to be RESTful)
    # CREATE, GET, UPDATE, DELETE (CGUD)
    'get_menus': {
        'url': 'menus',
        'method': 'get'
    },
    'get_menu': {
        'url': 'menus/{id}',
        'method': 'get'
    },
    'update_menu': {
        'url': 'menus/{id}',
        'method': 'put'
    },
    'delete_menu': {
        'url': 'menus/{id}',
        'method': 'delete'
    },
    'get_restaurants': {
        'url': 'restaurants',
        'method': 'get'
    },
    'get_tags': {
        'url': 'tags',
        'method': 'get'
    },
}


class APIService():
    """API Service (wrapper) to communicate with backend API Service (Snakebite)"""

    @classmethod
    def set_env(cls, env):
        cls.env = env

    def _get_base_url(self):
        return constants.API_SERVICE_URL_MAP[self.__class__.env]

    def __init__(self, token):
        self.token = token
        self.url = self._get_base_url()



    def _send_requests(self, url, method='get', params=None, payload=None):
        try:
            url = '/'.join([url, self.url])  # concatenate URL
            params.update({'token': self.token})  # add token for verification
            resp = requests.request(method, url, params=params, data=json.loads(payload))

            if resp.status_code >= 400:  # error occured
                raise Exception

            return resp.json() or resp.text  # return json body of response

        except Exception as e:
            raise APIException(e)

    def __getattr__(self, api_call, **kwargs):

        def _send_requests(url, method='get', params=None, payload=None):
            try:
                url = '/'.join([url, self.url])  # concatenate URL
                params.update({'token': self.token})  # add token for verification
                resp = requests.request(method, url, params=params, data=json.loads(payload))

                if resp.status_code >= 400:  # error occured
                    raise Exception

                return resp.json() or resp.text  # return json body of response

            except Exception as e:
                raise APIException(e)

        if api_call not in API_MAP:
            raise APIException('unsupported method')

        api = API_MAP[api_call]
        url_keys = Formatter().parse(api['url'])  # grab list of keys required to override with value in URL
        url = api['url'].format(**{key: kwargs.pop(key) for key in url_keys})  # pad URL with required keys (e.g., id)
        return _send_requests(url, api['method'], params=kwargs, payload=kwargs)
