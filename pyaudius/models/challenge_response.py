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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChallengeResponse(BaseModel):
    """
    ChallengeResponse
    """ # noqa: E501
    challenge_id: StrictStr
    user_id: StrictStr
    specifier: Optional[StrictStr] = None
    is_complete: StrictBool
    is_active: StrictBool
    is_disbursed: StrictBool
    current_step_count: Optional[StrictInt] = None
    max_steps: Optional[StrictInt] = None
    challenge_type: StrictStr
    amount: StrictStr
    disbursed_amount: StrictInt
    cooldown_days: Optional[StrictInt] = None
    metadata: Dict[str, Any]
    __properties: ClassVar[List[str]] = ["challenge_id", "user_id", "specifier", "is_complete", "is_active", "is_disbursed", "current_step_count", "max_steps", "challenge_type", "amount", "disbursed_amount", "cooldown_days", "metadata"]

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
        """Create an instance of ChallengeResponse from a JSON string"""
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
        """Create an instance of ChallengeResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "challenge_id": obj.get("challenge_id"),
            "user_id": obj.get("user_id"),
            "specifier": obj.get("specifier"),
            "is_complete": obj.get("is_complete"),
            "is_active": obj.get("is_active"),
            "is_disbursed": obj.get("is_disbursed"),
            "current_step_count": obj.get("current_step_count"),
            "max_steps": obj.get("max_steps"),
            "challenge_type": obj.get("challenge_type"),
            "amount": obj.get("amount"),
            "disbursed_amount": obj.get("disbursed_amount"),
            "cooldown_days": obj.get("cooldown_days"),
            "metadata": obj.get("metadata")
        })
        return _obj


