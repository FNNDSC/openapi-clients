# coding: utf-8

"""
    ChRIS Research Integration System: Ultron BackEnd (CUBE) API

    The ChRIS Ultron BackEnd (CUBE) is the core backend API of ChRIS. It manages ChRIS users, plugins, pipelines, and the provenance of data analyses as ChRIS feeds.

    The version of the OpenAPI document: ${GITHUB_REF_NAME:1}
    Contact: dev@babymri.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Feed(BaseModel):
    """
    Feed
    """ # noqa: E501
    url: StrictStr
    id: StrictInt
    creation_date: datetime
    modification_date: datetime
    name: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    public: Optional[StrictBool] = None
    owner_username: StrictStr = Field(description="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    folder_path: Optional[StrictStr]
    created_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'created' status.")
    waiting_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'waiting' status.")
    scheduled_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'scheduled' status.")
    started_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'started' status.")
    registering_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'registeringFiles' status.")
    finished_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'finishedSuccessfully' status.")
    errored_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'finishedWithError' status.")
    cancelled_jobs: StrictInt = Field(description="Overriden to get the number of plugin instances in 'cancelled' status.")
    folder: StrictStr
    note: StrictStr
    group_permissions: StrictStr
    user_permissions: StrictStr
    tags: StrictStr
    taggings: StrictStr
    comments: StrictStr
    plugin_instances: StrictStr
    owner: StrictStr
    __properties: ClassVar[List[str]] = ["url", "id", "creation_date", "modification_date", "name", "public", "owner_username", "folder_path", "created_jobs", "waiting_jobs", "scheduled_jobs", "started_jobs", "registering_jobs", "finished_jobs", "errored_jobs", "cancelled_jobs", "folder", "note", "group_permissions", "user_permissions", "tags", "taggings", "comments", "plugin_instances", "owner"]

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
        """Create an instance of Feed from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "url",
            "id",
            "creation_date",
            "modification_date",
            "owner_username",
            "folder_path",
            "created_jobs",
            "waiting_jobs",
            "scheduled_jobs",
            "started_jobs",
            "registering_jobs",
            "finished_jobs",
            "errored_jobs",
            "cancelled_jobs",
            "folder",
            "note",
            "group_permissions",
            "user_permissions",
            "tags",
            "taggings",
            "comments",
            "plugin_instances",
            "owner",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.folder_path is None and "folder_path" in self.model_fields_set:
            _dict['folder_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Feed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "id": obj.get("id"),
            "creation_date": obj.get("creation_date"),
            "modification_date": obj.get("modification_date"),
            "name": obj.get("name"),
            "public": obj.get("public"),
            "owner_username": obj.get("owner_username"),
            "folder_path": obj.get("folder_path"),
            "created_jobs": obj.get("created_jobs"),
            "waiting_jobs": obj.get("waiting_jobs"),
            "scheduled_jobs": obj.get("scheduled_jobs"),
            "started_jobs": obj.get("started_jobs"),
            "registering_jobs": obj.get("registering_jobs"),
            "finished_jobs": obj.get("finished_jobs"),
            "errored_jobs": obj.get("errored_jobs"),
            "cancelled_jobs": obj.get("cancelled_jobs"),
            "folder": obj.get("folder"),
            "note": obj.get("note"),
            "group_permissions": obj.get("group_permissions"),
            "user_permissions": obj.get("user_permissions"),
            "tags": obj.get("tags"),
            "taggings": obj.get("taggings"),
            "comments": obj.get("comments"),
            "plugin_instances": obj.get("plugin_instances"),
            "owner": obj.get("owner")
        })
        return _obj


