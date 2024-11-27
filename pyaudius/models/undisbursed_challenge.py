# coding: utf-8

"""
    API

    Audius V1 API

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UndisbursedChallenge(BaseModel):
    """
    UndisbursedChallenge
    """ # noqa: E501
    challenge_id: StrictStr
    user_id: StrictStr
    specifier: StrictStr
    amount: StrictStr
    completed_blocknumber: StrictInt
    handle: StrictStr
    wallet: StrictStr
    created_at: StrictStr
    completed_at: StrictStr
    cooldown_days: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["challenge_id", "user_id", "specifier", "amount", "completed_blocknumber", "handle", "wallet", "created_at", "completed_at", "cooldown_days"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UndisbursedChallenge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UndisbursedChallenge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "challenge_id": obj.get("challenge_id"),
            "user_id": obj.get("user_id"),
            "specifier": obj.get("specifier"),
            "amount": obj.get("amount"),
            "completed_blocknumber": obj.get("completed_blocknumber"),
            "handle": obj.get("handle"),
            "wallet": obj.get("wallet"),
            "created_at": obj.get("created_at"),
            "completed_at": obj.get("completed_at"),
            "cooldown_days": obj.get("cooldown_days")
        })
        return _obj


