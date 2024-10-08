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

from aiochris_oag.models.paginated_comment_list import PaginatedCommentList

class TestPaginatedCommentList(unittest.TestCase):
    """PaginatedCommentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedCommentList:
        """Test PaginatedCommentList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedCommentList`
        """
        model = PaginatedCommentList()
        if include_optional:
            return PaginatedCommentList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    aiochris_oag.models.comment.Comment(
                        url = '', 
                        id = 56, 
                        title = '', 
                        owner_username = '', 
                        content = '', 
                        feed = '', )
                    ]
            )
        else:
            return PaginatedCommentList(
        )
        """

    def testPaginatedCommentList(self):
        """Test PaginatedCommentList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
