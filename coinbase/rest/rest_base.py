import json
import os
from typing import Optional

import requests
from requests.exceptions import HTTPError

from coinbase import jwt_generator
from coinbase.__version__ import __version__
from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY, BASE_URL


def prepare_params(params):
    if params is None:
        return None

    def encode_value(key, value):
        if isinstance(value, list):
            return "&".join(f"{key}={v}" for v in value)
        else:
            return f"{key}={value}"

    return "&".join(encode_value(key, value) for key, value in params.items())


def encode(data):
    if data is None:
        return None
    return json.dumps(data).encode("utf-8")


def handle_exception(response):
    """Raises :class:`HTTPError`, if one occurred."""

    http_error_msg = ""
    reason = response.reason

    if 400 <= response.status_code < 500:
        http_error_msg = (
            f"{response.status_code} Client Error: {reason} {response.text}"
        )

    elif 500 <= response.status_code < 600:
        http_error_msg = (
            f"{response.status_code} Server Error: {reason} {response.text}"
        )

    if http_error_msg:
        raise HTTPError(http_error_msg, response=response)


class RESTBase(object):
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(API_ENV_KEY),
        api_secret: Optional[str] = os.getenv(API_SECRET_ENV_KEY),
        base_url=BASE_URL,
        timeout=None,
    ):
        if api_key is None:
            raise Exception(
                f"Must specify env var COINBASE_API_KEY or pass api_key in constructor"
            )
        if api_secret is None:
            raise Exception(
                f"Must specify env var COINBASE_API_SECRET or pass api_secret in constructor"
            )
        self.api_key = api_key
        self.api_secret = bytes(api_secret, encoding="utf8").decode("unicode_escape")
        self.base_url = base_url
        self.timeout = timeout

    def get(self, url_path, params: Optional[dict] = None):
        return self.prepare_and_send_request("GET", url_path, params, data=None)

    def post(
        self, url_path, params: Optional[dict] = None, data: Optional[dict] = None
    ):
        return self.prepare_and_send_request("POST", url_path, params, data)

    def put(self, url_path, params: Optional[dict] = None, data: Optional[dict] = None):
        return self.prepare_and_send_request("PUT", url_path, params, data)

    def delete(
        self, url_path, params: Optional[dict] = None, data: Optional[dict] = None
    ):
        return self.prepare_and_send_request("DELETE", url_path, params, data)

    def prepare_and_send_request(
        self,
        http_method,
        url_path,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        headers = self.set_headers(http_method, url_path)

        params_string = prepare_params(params)
        if params_string:
            url_path = f"{url_path}?{params_string}"

        data_encoded = encode(data)
        return self.send_request(http_method, url_path, headers, data=data_encoded)

    def send_request(self, http_method, url_path, headers, data=None):
        if data is None:
            data = {}

        url = f"https://{self.base_url}{url_path}"

        response = requests.request(
            http_method, url, data=data, headers=headers, timeout=self.timeout
        )
        handle_exception(response)  # Raise an HTTPError for bad responses

        return response.json()

    def set_headers(self, method, path):
        uri = f"{method} {self.base_url}{path}"
        jwt = jwt_generator.build_rest_jwt(uri, self.api_key, self.api_secret)
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + jwt,
            "User-Agent": "coinbase-advanced-py/" + __version__,
        }
