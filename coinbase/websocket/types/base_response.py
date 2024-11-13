from typing import Any


class BaseResponse:
    def __init__(self, **data):
        for key in list(data.keys()):
            setattr(self, key, data.pop(key))

    def __getitem__(self, key: str) -> Any:
        return self.__dict__.get(key)

    def __repr__(self):
        return str(self.__dict__)
