# coding: utf-8

"""
    ChRIS Research Integration System: Ultron BackEnd (CUBE) API

    The ChRIS Ultron BackEnd (CUBE) is the core backend API of ChRIS. It manages ChRIS users, plugins, pipelines, and the provenance of data analyses as ChRIS feeds.

    The version of the OpenAPI document: 0.0.0+unknown
    Contact: dev@babymri.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from chris_oag.models.auth_token_request import AuthTokenRequest

class TestAuthTokenRequest(unittest.TestCase):
    """AuthTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthTokenRequest:
        """Test AuthTokenRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthTokenRequest`
        """
        model = AuthTokenRequest()
        if include_optional:
            return AuthTokenRequest(
                username = '0',
                password = '0'
            )
        else:
            return AuthTokenRequest(
                username = '0',
                password = '0',
        )
        """

    def testAuthTokenRequest(self):
        """Test AuthTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
