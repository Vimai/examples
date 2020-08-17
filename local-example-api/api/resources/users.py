import os
import json
import falcon
import logging
import requests

from datetime import datetime
from decimal import Decimal
from requests.exceptions import HTTPError


class Users:
    def __init__(self):
        self.logger = logging.getLogger('thingsapp.' + __name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(name)s - %(message)s')

        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def on_get(self, req, res):
        self.logger.info(f'Start: GET')
        res.status = falcon.get_http_status(status_code=200)

        response = [
            {
                'id': 1,
                'name': 'ana',
                'age': 25,
            },
            {
                'id': 2,
                'name': 'joao',
                'age': 25,
            }
        ]

        res.body = json.dumps(response)
        self.logger.info(f'End.')

    def on_post(self, req, res):
        self.logger.info(f'Start: POST')
        body = req.stream.read(req.content_length or 0)
        try:
            body = json.loads(body.decode('utf-8'), parse_float=Decimal)
        except ValueError as err:
            res.status = falcon.get_http_status(status_code=400)
            response = {
                "msg": 'not a valid json',
            }
            res.body = json.dumps(response)
            self.logger.info(f'End.')
            return

        res.status = falcon.get_http_status(status_code=200)

        chose = 0
        if 'choice' in body:
            if body['choice'] in (1, 2):
                chose = body['choice']

            response_dict = {
                "msg": f'chose {chose}' if chose else 'chose default',
            }
        else:
            res.status = falcon.get_http_status(status_code=400)
            response_dict = {
                "msg": 'choice not passed',
            }

        res.body = json.dumps(response_dict)
        self.logger.info(f'End.')