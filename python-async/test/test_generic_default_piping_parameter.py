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

from aiochris_oag.models.generic_default_piping_parameter import GenericDefaultPipingParameter

class TestGenericDefaultPipingParameter(unittest.TestCase):
    """GenericDefaultPipingParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenericDefaultPipingParameter:
        """Test GenericDefaultPipingParameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenericDefaultPipingParameter`
        """
        model = GenericDefaultPipingParameter()
        if include_optional:
            return GenericDefaultPipingParameter(
                url = '',
                id = 56,
                value = None,
                type = 'string',
                plugin_piping_id = 56,
                plugin_piping_title = '',
                previous_plugin_piping_id = 56,
                param_name = '',
                param_id = 56,
                plugin_piping = '',
                plugin_name = '',
                plugin_version = '',
                plugin_id = 56,
                plugin_param = ''
            )
        else:
            return GenericDefaultPipingParameter(
                url = '',
                id = 56,
                value = None,
                type = 'string',
                plugin_piping_id = 56,
                plugin_piping_title = '',
                previous_plugin_piping_id = 56,
                param_name = '',
                param_id = 56,
                plugin_piping = '',
                plugin_name = '',
                plugin_version = '',
                plugin_id = 56,
                plugin_param = '',
        )
        """

    def testGenericDefaultPipingParameter(self):
        """Test GenericDefaultPipingParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
