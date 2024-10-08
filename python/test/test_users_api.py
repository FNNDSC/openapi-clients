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

from chris_oag.api.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()

    def tearDown(self) -> None:
        pass

    def test_users_create(self) -> None:
        """Test case for users_create

        """
        pass

    def test_users_groups_list(self) -> None:
        """Test case for users_groups_list

        """
        pass

    def test_users_list(self) -> None:
        """Test case for users_list

        """
        pass

    def test_users_retrieve(self) -> None:
        """Test case for users_retrieve

        """
        pass

    def test_users_update(self) -> None:
        """Test case for users_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
