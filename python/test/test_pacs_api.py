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

from chris_oag.api.pacs_api import PacsApi


class TestPacsApi(unittest.TestCase):
    """PacsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PacsApi()

    def tearDown(self) -> None:
        pass

    def test_pacs_files_list(self) -> None:
        """Test case for pacs_files_list

        """
        pass

    def test_pacs_files_retrieve(self) -> None:
        """Test case for pacs_files_retrieve

        """
        pass

    def test_pacs_files_retrieve_0(self) -> None:
        """Test case for pacs_files_retrieve_0

        """
        pass

    def test_pacs_files_search_list(self) -> None:
        """Test case for pacs_files_search_list

        """
        pass

    def test_pacs_series_list(self) -> None:
        """Test case for pacs_series_list

        """
        pass

    def test_pacs_series_retrieve(self) -> None:
        """Test case for pacs_series_retrieve

        """
        pass

    def test_pacs_series_search_list(self) -> None:
        """Test case for pacs_series_search_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
