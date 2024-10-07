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

from aiochris_oag.models.feed_user_permission_request import FeedUserPermissionRequest

class TestFeedUserPermissionRequest(unittest.TestCase):
    """FeedUserPermissionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeedUserPermissionRequest:
        """Test FeedUserPermissionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeedUserPermissionRequest`
        """
        model = FeedUserPermissionRequest()
        if include_optional:
            return FeedUserPermissionRequest(
                username = '0123'
            )
        else:
            return FeedUserPermissionRequest(
                username = '0123',
        )
        """

    def testFeedUserPermissionRequest(self):
        """Test FeedUserPermissionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
