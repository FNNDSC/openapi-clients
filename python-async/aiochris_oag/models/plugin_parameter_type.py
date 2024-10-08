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
import json
from enum import Enum
from typing_extensions import Self


class PluginParameterType(str, Enum):
    """
    * `string` - String values * `float` - Float values * `boolean` - Boolean values * `integer` - Integer values * `path` - Path values * `unextpath` - Unextracted path values
    """

    """
    allowed enum values
    """
    STRING = 'string'
    FLOAT = 'float'
    BOOLEAN = 'boolean'
    INTEGER = 'integer'
    PATH = 'path'
    UNEXTPATH = 'unextpath'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PluginParameterType from a JSON string"""
        return cls(json.loads(json_str))


