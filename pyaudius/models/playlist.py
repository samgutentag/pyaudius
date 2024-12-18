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
from pyaudius.models.access import Access
from pyaudius.models.playlist_added_timestamp import PlaylistAddedTimestamp
from pyaudius.models.playlist_artwork import PlaylistArtwork
from pyaudius.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class Playlist(BaseModel):
    """
    Playlist
    """ # noqa: E501
    artwork: Optional[PlaylistArtwork] = None
    description: Optional[StrictStr] = None
    permalink: StrictStr
    id: StrictStr
    is_album: StrictBool
    is_image_autogenerated: StrictBool
    playlist_name: StrictStr
    playlist_contents: List[PlaylistAddedTimestamp]
    repost_count: StrictInt
    favorite_count: StrictInt
    total_play_count: StrictInt
    user: User
    ddex_app: Optional[StrictStr] = None
    access: Access
    upc: Optional[StrictStr] = None
    track_count: StrictInt
    __properties: ClassVar[List[str]] = ["artwork", "description", "permalink", "id", "is_album", "is_image_autogenerated", "playlist_name", "playlist_contents", "repost_count", "favorite_count", "total_play_count", "user", "ddex_app", "access", "upc", "track_count"]

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
        """Create an instance of Playlist from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of artwork
        if self.artwork:
            _dict['artwork'] = self.artwork.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in playlist_contents (list)
        _items = []
        if self.playlist_contents:
            for _item_playlist_contents in self.playlist_contents:
                if _item_playlist_contents:
                    _items.append(_item_playlist_contents.to_dict())
            _dict['playlist_contents'] = _items
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of access
        if self.access:
            _dict['access'] = self.access.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Playlist from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "artwork": PlaylistArtwork.from_dict(obj["artwork"]) if obj.get("artwork") is not None else None,
            "description": obj.get("description"),
            "permalink": obj.get("permalink"),
            "id": obj.get("id"),
            "is_album": obj.get("is_album"),
            "is_image_autogenerated": obj.get("is_image_autogenerated"),
            "playlist_name": obj.get("playlist_name"),
            "playlist_contents": [PlaylistAddedTimestamp.from_dict(_item) for _item in obj["playlist_contents"]] if obj.get("playlist_contents") is not None else None,
            "repost_count": obj.get("repost_count"),
            "favorite_count": obj.get("favorite_count"),
            "total_play_count": obj.get("total_play_count"),
            "user": User.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "ddex_app": obj.get("ddex_app"),
            "access": Access.from_dict(obj["access"]) if obj.get("access") is not None else None,
            "upc": obj.get("upc"),
            "track_count": obj.get("track_count")
        })
        return _obj


