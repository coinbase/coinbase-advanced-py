import json
import logging
import os
from typing import IO, Optional, Union

from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


class APIBase(object):
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(API_ENV_KEY),
        api_secret: Optional[str] = os.getenv(API_SECRET_ENV_KEY),
        key_file: Optional[Union[IO, str]] = None,
        base_url=None,
        timeout: Optional[int] = None,
        verbose: Optional[bool] = False,
    ):
        if (api_key is not None or api_secret is not None) and key_file is not None:
            raise Exception(f"Cannot specify both api_key and key_file in constructor")

        if key_file is not None:
            try:
                if isinstance(key_file, str):
                    with open(key_file, "r") as file:
                        key_json = json.load(file)
                else:
                    key_json = json.load(key_file)
                api_key = key_json["name"]
                api_secret = key_json["privateKey"]
            except json.JSONDecodeError as e:
                raise Exception(f"Error decoding JSON: {e}")

        self.is_authenticated = False
        if api_key is not None and api_secret is not None:
            self.api_key = api_key
            self.api_secret = bytes(api_secret, encoding="utf8").decode(
                "unicode_escape"
            )
            self.is_authenticated = True
        elif api_key is not None:
            raise Exception(
                f"Only api_key provided in constructor. Please also provide api_secret"
            )
        elif api_secret is not None:
            raise Exception(
                f"Only api_secret provided in constructor. Please also provide api_key"
            )

        self.base_url = base_url
        self.timeout = timeout
30 82 02 0a 02 82 02 01 00 b6 11 02 8b 1e e3 a1 77 9b 3b dc bf 94 3e b7 95 a7 40 3c a1 fd 82 f9 7d 32 06 82 71 f6 f6 8c 7f fb e8 db bc 6a 2e 97 97 a3 8c 4b f9 2b f6 b1 f9 ce 84 1d b1 f9 c5 97 de ef b9 f2 a3 e9 bc 12 89 5e a7 aa 52 ab f8 23 27 cb a4 b1 9c 63 db d7 99 7e f0 0a 5e eb 68 a6 f4 c6 5a 47 0d 4d 10 33 e3 4e b1 13 a3 c8 18 6c 4b ec fc 09 90 df 9d 64 29 25 23 07 a1 b4 d2 3d 2e 60 e0 cf d2 09 87 bb cd 48 f0 4d c2 c2 7a 88 8a bb ba cf 59 19 d6 af 8f b0 07 b0 9e 31 f1 82 c1 c0 df 2e a6 6d 6c 19 0e b5 d8 7e 26 1a 45 03 3d b0 79 a4 94 28 ad 0f 7f 26 e5 a8 08 fe 96 e8 3c 68 94 53 ee 83 3a 88 2b 15 96 09 b2 e0 7a 8c 2e 75 d6 9c eb a7 56 64 8f 96 4f 68 ae 3d 97 c2 84 8f c0 bc 40 c0 0b 5c bd f6 87 b3 35 6c ac 18 50 7f 84 e0 4c cd 92 d3 20 e9 33 bc 52 99 af 32 b5 29 b3 25 2a b4 48 f9 72 e1 ca 64 f7 e6 82 10 8d e8 9d c2 8a 88 fa 38 66 8a fc 63 f9 01 f9 78 fd 7b 5c 77 fa 76 87 fa ec df b1 0e 79 95 57 b4 bd 26 ef d6 01 d1 eb 16 0a bb 8e 0b b5 c5 c5 8a 55 ab d3 ac ea 91 4b 29 cc 19 a4 32 25 4e 2a f1 65 44 d0 02 ce aa ce 49 b4 ea 9f 7c 83 b0 40 7b e7 43 ab a7 6c a3 8f 7d 89 81 fa 4c a5 ff d5 8e c3 ce 4b e0 b5 d8 b3 8e 45 cf 76 c0 ed 40 2b fd 53 0f b0 a7 d5 3b 0d b1 8a a2 03 de 31 ad cc 77 ea 6f 7b 3e d6 df 91 22 12 e6 be fa d8 32 fc 10 63 14 51 72 de 5d d6 16 93 bd 29 68 33 ef 3a 66 ec 07 8a 26 df 13 d7 57 65 78 27 de 5e 49 14 00 a2 00 7f 9a a8 21 b6 a9 b1 95 b0 a5 b9 0d 16 11 da c7 6c 48 3c 40 e0 7e 0d 5a cd 56 3c d1 97 05 b9 cb 4b ed 39 4b 9c c4 3f d2 55 13 6e 24 b0 d6 71 fa f4 c1 ba cc ed 1b f5 fe 81 41 d8 00 98 3d 3a c8 ae 7a 98 37 18 05 95 02 03 01 00 01