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

from chris_oag.models.paginated_tag_list import PaginatedTagList

class TestPaginatedTagList(unittest.TestCase):
    """PaginatedTagList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedTagList:
        """Test PaginatedTagList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedTagList`
        """
        model = PaginatedTagList()
        if include_optional:
            return PaginatedTagList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    chris_oag.models.tag.Tag(
                        url = '', 
                        id = 56, 
                        name = '', 
                        owner_username = '', 
                        color = '', 
                        feeds = '', 
                        taggings = '', )
                    ]
            )
        else:
            return PaginatedTagList(
        )
        """

    def testPaginatedTagList(self):
        """Test PaginatedTagList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
