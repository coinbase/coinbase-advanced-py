from typing import Dict, Tuple, Type

from coinbase.rest.types.base_response import BaseResponse


class DeribitModel(BaseResponse):
    """Base for generated Deribit response models.

    Same attribute-access + ``to_dict()`` contract as the spot SDK's BaseResponse,
    extended with a generated ``_NESTED`` map so nested objects and lists of objects
    deserialize into their own typed models instead of staying raw dicts.

    ``_NESTED`` maps a field name to ``(ModelClass, is_list)``. Subclasses are
    emitted by ``scripts/generate_deribit.py`` — do not hand-edit them.
    """

    _NESTED: Dict[str, Tuple[Type["DeribitModel"], bool]] = {}

    def __init__(self, response: dict):
        response = dict(response) if response else {}
        for field, (model, _is_list) in self._NESTED.items():
            if field not in response or response[field] is None:
                continue
            value = response.pop(field)
            # Follow the shape the gateway actually returned. The spec and the
            # gateway sometimes disagree on list vs object; never drop data.
            if isinstance(value, list):
                setattr(
                    self,
                    field,
                    [model(item) if isinstance(item, dict) else item for item in value],
                )
            elif isinstance(value, dict):
                setattr(self, field, model(value))
            else:
                setattr(self, field, value)
        super().__init__(**response)
