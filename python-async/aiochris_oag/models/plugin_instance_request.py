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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from aiochris_oag.models.status_enum import StatusEnum
from typing import Optional, Set
from typing_extensions import Self

class PluginInstanceRequest(BaseModel):
    """
    PluginInstanceRequest
    """ # noqa: E501
    title: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    compute_resource_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = None
    status: Optional[StatusEnum] = None
    cpu_limit: Optional[StrictInt] = None
    memory_limit: Optional[StrictInt] = None
    number_of_workers: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    gpu_limit: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    previous_id: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["title", "compute_resource_name", "status", "cpu_limit", "memory_limit", "number_of_workers", "gpu_limit", "previous_id"]

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
        """Create an instance of PluginInstanceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

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

        # set to None if previous_id (nullable) is None
        # and model_fields_set contains the field
        if self.previous_id is None and "previous_id" in self.model_fields_set:
            _dict['previous_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PluginInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "compute_resource_name": obj.get("compute_resource_name"),
            "status": obj.get("status"),
            "cpu_limit": obj.get("cpu_limit"),
            "memory_limit": obj.get("memory_limit"),
            "number_of_workers": obj.get("number_of_workers"),
            "gpu_limit": obj.get("gpu_limit"),
            "previous_id": obj.get("previous_id")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


