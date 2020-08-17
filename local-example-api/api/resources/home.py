import os
import json
import falcon
import logging
import requests

from datetime import datetime
from decimal import Decimal
from requests.exceptions import HTTPError


class Home:
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

        response = {
            'ids': [1, 2]
        }

        res.body = json.dumps(response)
        self.logger.info(f'End.')
