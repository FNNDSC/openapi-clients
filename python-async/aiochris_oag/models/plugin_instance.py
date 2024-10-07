# coding: utf-8

"""
    ChRIS Research Integration System: Ultron BackEnd (CUBE) API

    The ChRIS Ultron BackEnd (CUBE) is the core backend API of ChRIS. It manages ChRIS users, plugins, pipelines, and the provenance of data analyses as ChRIS feeds.

    The version of the OpenAPI document: 0.0.0+unknown
    Contact: dev@babymri.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from aiochris_oag.models.plugin_type import PluginType
from aiochris_oag.models.status_enum import StatusEnum
from typing import Optional, Set
from typing_extensions import Self

class PluginInstance(BaseModel):
    """
    PluginInstance
    """ # noqa: E501
    url: StrictStr
    id: StrictInt
    title: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    previous_id: Optional[StrictInt]
    compute_resource_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    plugin_id: StrictInt
    plugin_name: StrictStr
    plugin_version: StrictStr
    plugin_type: PluginType
    feed_id: StrictInt
    start_date: datetime
    end_date: datetime
    output_path: Optional[StrictStr]
    status: Optional[StatusEnum] = None
    pipeline_id: Optional[StrictInt]
    pipeline_name: Optional[StrictStr]
    workflow_id: Optional[StrictInt]
    summary: StrictStr
    raw: StrictStr
    owner_username: StrictStr = Field(description="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    cpu_limit: Optional[StrictInt] = None
    memory_limit: Optional[StrictInt] = None
    number_of_workers: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    gpu_limit: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    size: Annotated[int, Field(le=9223372036854775807, strict=True, ge=-9223372036854775808)]
    error_code: StrictStr
    output_folder: StrictStr
    previous: Optional[StrictStr]
    feed: StrictStr
    plugin: StrictStr
    workflow: Optional[StrictStr]
    compute_resource: StrictStr
    descendants: StrictStr
    parameters: StrictStr
    splits: StrictStr
    __properties: ClassVar[List[str]] = ["url", "id", "title", "previous_id", "compute_resource_name", "plugin_id", "plugin_name", "plugin_version", "plugin_type", "feed_id", "start_date", "end_date", "output_path", "status", "pipeline_id", "pipeline_name", "workflow_id", "summary", "raw", "owner_username", "cpu_limit", "memory_limit", "number_of_workers", "gpu_limit", "size", "error_code", "output_folder", "previous", "feed", "plugin", "workflow", "compute_resource", "descendants", "parameters", "splits"]

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
        """Create an instance of PluginInstance from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "url",
            "id",
            "previous_id",
            "plugin_id",
            "plugin_name",
            "plugin_version",
            "plugin_type",
            "feed_id",
            "start_date",
            "end_date",
            "output_path",
            "pipeline_id",
            "pipeline_name",
            "workflow_id",
            "summary",
            "raw",
            "owner_username",
            "size",
            "error_code",
            "output_folder",
            "previous",
            "feed",
            "plugin",
            "workflow",
            "compute_resource",
            "descendants",
            "parameters",
            "splits",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if previous_id (nullable) is None
        # and model_fields_set contains the field
        if self.previous_id is None and "previous_id" in self.model_fields_set:
            _dict['previous_id'] = None

        # set to None if output_path (nullable) is None
        # and model_fields_set contains the field
        if self.output_path is None and "output_path" in self.model_fields_set:
            _dict['output_path'] = None

        # set to None if pipeline_id (nullable) is None
        # and model_fields_set contains the field
        if self.pipeline_id is None and "pipeline_id" in self.model_fields_set:
            _dict['pipeline_id'] = None

        # set to None if pipeline_name (nullable) is None
        # and model_fields_set contains the field
        if self.pipeline_name is None and "pipeline_name" in self.model_fields_set:
            _dict['pipeline_name'] = None

        # set to None if workflow_id (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_id is None and "workflow_id" in self.model_fields_set:
            _dict['workflow_id'] = None

        # set to None if cpu_limit (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_limit is None and "cpu_limit" in self.model_fields_set:
            _dict['cpu_limit'] = None

        # set to None if memory_limit (nullable) is None
        # and model_fields_set contains the field
        if self.memory_limit is None and "memory_limit" in self.model_fields_set:
            _dict['memory_limit'] = None

        # set to None if number_of_workers (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_workers is None and "number_of_workers" in self.model_fields_set:
            _dict['number_of_workers'] = None

        # set to None if gpu_limit (nullable) is None
        # and model_fields_set contains the field
        if self.gpu_limit is None and "gpu_limit" in self.model_fields_set:
            _dict['gpu_limit'] = None

        # set to None if previous (nullable) is None
        # and model_fields_set contains the field
        if self.previous is None and "previous" in self.model_fields_set:
            _dict['previous'] = None

        # set to None if workflow (nullable) is None
        # and model_fields_set contains the field
        if self.workflow is None and "workflow" in self.model_fields_set:
            _dict['workflow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PluginInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "id": obj.get("id"),
            "title": obj.get("title"),
            "previous_id": obj.get("previous_id"),
            "compute_resource_name": obj.get("compute_resource_name"),
            "plugin_id": obj.get("plugin_id"),
            "plugin_name": obj.get("plugin_name"),
            "plugin_version": obj.get("plugin_version"),
            "plugin_type": obj.get("plugin_type"),
            "feed_id": obj.get("feed_id"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "output_path": obj.get("output_path"),
            "status": obj.get("status"),
            "pipeline_id": obj.get("pipeline_id"),
            "pipeline_name": obj.get("pipeline_name"),
            "workflow_id": obj.get("workflow_id"),
            "summary": obj.get("summary"),
            "raw": obj.get("raw"),
            "owner_username": obj.get("owner_username"),
            "cpu_limit": obj.get("cpu_limit"),
            "memory_limit": obj.get("memory_limit"),
            "number_of_workers": obj.get("number_of_workers"),
            "gpu_limit": obj.get("gpu_limit"),
            "size": obj.get("size"),
            "error_code": obj.get("error_code"),
            "output_folder": obj.get("output_folder"),
            "previous": obj.get("previous"),
            "feed": obj.get("feed"),
            "plugin": obj.get("plugin"),
            "workflow": obj.get("workflow"),
            "compute_resource": obj.get("compute_resource"),
            "descendants": obj.get("descendants"),
            "parameters": obj.get("parameters"),
            "splits": obj.get("splits")
        })
        return _obj


