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

from chris_oag.models.file_browser_file_group_permission import FileBrowserFileGroupPermission

class TestFileBrowserFileGroupPermission(unittest.TestCase):
    """FileBrowserFileGroupPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileBrowserFileGroupPermission:
        """Test FileBrowserFileGroupPermission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileBrowserFileGroupPermission`
        """
        model = FileBrowserFileGroupPermission()
        if include_optional:
            return FileBrowserFileGroupPermission(
                url = '',
                id = 56,
                permission = 'r',
                file_id = 56,
                file_fname = '',
                group_id = 56,
                group_name = '',
                file = '',
                group = ''
            )
        else:
            return FileBrowserFileGroupPermission(
                url = '',
                id = 56,
                file_id = 56,
                file_fname = '',
                group_id = 56,
                group_name = '',
                file = '',
                group = '',
        )
        """

    def testFileBrowserFileGroupPermission(self):
        """Test FileBrowserFileGroupPermission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
