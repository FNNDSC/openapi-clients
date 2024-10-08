# coding: utf-8

"""
    ChRIS Research Integration System: Ultron BackEnd (CUBE) API

    The ChRIS Ultron BackEnd (CUBE) is the core backend API of ChRIS. It manages ChRIS users, plugins, pipelines, and the provenance of data analyses as ChRIS feeds.

    The version of the OpenAPI document: ${GITHUB_REF_NAME:1}
    Contact: dev@babymri.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chris_oag.api.plugininstances_api import PlugininstancesApi


class TestPlugininstancesApi(unittest.TestCase):
    """PlugininstancesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PlugininstancesApi()

    def tearDown(self) -> None:
        pass

    def test_plugininstances_list(self) -> None:
        """Test case for plugininstances_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
