from typing import Any

common_fields = {
    "x-ratelimit-remaining": "rate_limit_remaining",
    "x-ratelimit-reset": "rate_limit_reset",
    "x-ratelimit-limit": "rate_limit_limit",
}


class BaseResponse:
    def __init__(self, **kwargs):
        for field, formattedField in common_fields.items():
            if field in kwargs:
                setattr(self, formattedField, kwargs.pop(field))

        for key in list(kwargs.keys()):
            setattr(self, key, kwargs.pop(key))

    def __getitem__(self, key: str) -> Any:
        return self.__dict__.get(key)

    def __repr__(self):
        return str(self.__dict__)
