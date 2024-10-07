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

from chris_oag.api.comments_api import CommentsApi


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommentsApi()

    def tearDown(self) -> None:
        pass

    def test_comments_create(self) -> None:
        """Test case for comments_create

        """
        pass

    def test_comments_destroy(self) -> None:
        """Test case for comments_destroy

        """
        pass

    def test_comments_list(self) -> None:
        """Test case for comments_list

        """
        pass

    def test_comments_retrieve(self) -> None:
        """Test case for comments_retrieve

        """
        pass

    def test_comments_search_list(self) -> None:
        """Test case for comments_search_list

        """
        pass

    def test_comments_update(self) -> None:
        """Test case for comments_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
