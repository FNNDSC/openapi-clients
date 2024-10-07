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
import json
from enum import Enum
from typing_extensions import Self


class StatusEnum(str, Enum):
    """
    * `created` - Default initial * `waiting` - Waiting to be scheduled * `scheduled` - Scheduled on worker * `started` - Started on compute env * `registeringFiles` - Registering output files * `finishedSuccessfully` - Finished successfully * `finishedWithError` - Finished with error * `cancelled` - Cancelled
    """

    """
    allowed enum values
    """
    CREATED = 'created'
    WAITING = 'waiting'
    SCHEDULED = 'scheduled'
    STARTED = 'started'
    REGISTERINGFILES = 'registeringFiles'
    FINISHEDSUCCESSFULLY = 'finishedSuccessfully'
    FINISHEDWITHERROR = 'finishedWithError'
    CANCELLED = 'cancelled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusEnum from a JSON string"""
        return cls(json.loads(json_str))


