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

from aiochris_oag.models.tag import Tag

class TestTag(unittest.TestCase):
    """Tag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tag:
        """Test Tag
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tag`
        """
        model = Tag()
        if include_optional:
            return Tag(
                url = '',
                id = 56,
                name = '',
                owner_username = '',
                color = '',
                feeds = '',
                taggings = ''
            )
        else:
            return Tag(
                url = '',
                id = 56,
                owner_username = '',
                color = '',
                feeds = '',
                taggings = '',
        )
        """

    def testTag(self):
        """Test Tag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
