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

from chris_oag.models.default_piping_int_parameter_request import DefaultPipingIntParameterRequest

class TestDefaultPipingIntParameterRequest(unittest.TestCase):
    """DefaultPipingIntParameterRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DefaultPipingIntParameterRequest:
        """Test DefaultPipingIntParameterRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DefaultPipingIntParameterRequest`
        """
        model = DefaultPipingIntParameterRequest()
        if include_optional:
            return DefaultPipingIntParameterRequest(
                value = -2147483648
            )
        else:
            return DefaultPipingIntParameterRequest(
        )
        """

    def testDefaultPipingIntParameterRequest(self):
        """Test DefaultPipingIntParameterRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
