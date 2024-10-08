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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from chris_oag.models.plugin_parameter_type import PluginParameterType
from typing import Optional, Set
from typing_extensions import Self

class DefaultPipingStrParameter(BaseModel):
    """
    DefaultPipingStrParameter
    """ # noqa: E501
    url: StrictStr
    id: StrictInt
    value: Optional[Annotated[str, Field(strict=True, max_length=600)]] = None
    type: PluginParameterType
    plugin_piping_id: StrictInt
    plugin_piping_title: StrictStr
    previous_plugin_piping_id: Optional[StrictInt]
    param_name: StrictStr
    param_id: StrictInt
    plugin_piping: StrictStr
    plugin_name: StrictStr
    plugin_version: StrictStr
    plugin_id: StrictInt
    plugin_param: StrictStr
    __properties: ClassVar[List[str]] = ["url", "id", "value", "type", "plugin_piping_id", "plugin_piping_title", "previous_plugin_piping_id", "param_name", "param_id", "plugin_piping", "plugin_name", "plugin_version", "plugin_id", "plugin_param"]

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
        """Create an instance of DefaultPipingStrParameter from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "url",
            "id",
            "type",
            "plugin_piping_id",
            "plugin_piping_title",
            "previous_plugin_piping_id",
            "param_name",
            "param_id",
            "plugin_piping",
            "plugin_name",
            "plugin_version",
            "plugin_id",
            "plugin_param",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if previous_plugin_piping_id (nullable) is None
        # and model_fields_set contains the field
        if self.previous_plugin_piping_id is None and "previous_plugin_piping_id" in self.model_fields_set:
            _dict['previous_plugin_piping_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DefaultPipingStrParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "id": obj.get("id"),
            "value": obj.get("value"),
            "type": obj.get("type"),
            "plugin_piping_id": obj.get("plugin_piping_id"),
            "plugin_piping_title": obj.get("plugin_piping_title"),
            "previous_plugin_piping_id": obj.get("previous_plugin_piping_id"),
            "param_name": obj.get("param_name"),
            "param_id": obj.get("param_id"),
            "plugin_piping": obj.get("plugin_piping"),
            "plugin_name": obj.get("plugin_name"),
            "plugin_version": obj.get("plugin_version"),
            "plugin_id": obj.get("plugin_id"),
            "plugin_param": obj.get("plugin_param")
        })
        return _obj


