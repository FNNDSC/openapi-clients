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

from chris_oag.models.plugin_parameter import PluginParameter

class TestPluginParameter(unittest.TestCase):
    """PluginParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PluginParameter:
        """Test PluginParameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PluginParameter`
        """
        model = PluginParameter()
        if include_optional:
            return PluginParameter(
                url = '',
                id = 56,
                name = '',
                type = 'string',
                optional = True,
                default = None,
                flag = '',
                short_flag = '',
                action = '',
                help = '',
                ui_exposed = True,
                plugin = ''
            )
        else:
            return PluginParameter(
                url = '',
                id = 56,
                name = '',
                default = None,
                flag = '',
                plugin = '',
        )
        """

    def testPluginParameter(self):
        """Test PluginParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
