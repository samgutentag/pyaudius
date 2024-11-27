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

from pydantic import ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from pyaudius.models.activity import Activity
from pyaudius.models.track import Track
from typing import Optional, Set
from typing_extensions import Self

class TrackActivity(Activity):
    """
    TrackActivity
    """ # noqa: E501
    item_type: StrictStr
    item: Track
    __properties: ClassVar[List[str]] = ["timestamp", "item_type", "item", "class"]

    @field_validator('item_type')
    def item_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['track']):
            raise ValueError("must be one of enum values ('track')")
        return value

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
        """Create an instance of TrackActivity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrackActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "item_type": obj.get("item_type"),
            "item": Track.from_dict(obj["item"]) if obj.get("item") is not None else None,
            "class": obj.get("class")
        })
        return _obj


