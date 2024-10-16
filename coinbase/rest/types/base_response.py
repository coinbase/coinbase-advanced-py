from typing import Any

common_fields = {
    "x-ratelimit-remaining": "rate_limit_remaining",
    "x-ratelimit-reset": "rate_limit_reset",
    "x-ratelimit-limit": "rate_limit_limit",
}


class BaseResponse:
    def __init__(self, **kwargs):
        for field in list(kwargs.keys()):
            attr_name = field.replace("-", "_")

            if field in kwargs:
                setattr(self, attr_name, kwargs.pop(field))

        for key in list(kwargs.keys()):
            setattr(self, key, kwargs.pop(key))

    def __getitem__(self, key: str) -> Any:
        return self.__dict__.get(key)

    def __repr__(self):
        return str(self.__dict__)
