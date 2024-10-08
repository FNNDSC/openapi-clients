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

from aiochris_oag.models.file_browser_link_file_group_permission_request import FileBrowserLinkFileGroupPermissionRequest

class TestFileBrowserLinkFileGroupPermissionRequest(unittest.TestCase):
    """FileBrowserLinkFileGroupPermissionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileBrowserLinkFileGroupPermissionRequest:
        """Test FileBrowserLinkFileGroupPermissionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileBrowserLinkFileGroupPermissionRequest`
        """
        model = FileBrowserLinkFileGroupPermissionRequest()
        if include_optional:
            return FileBrowserLinkFileGroupPermissionRequest(
                permission = 'r',
                grp_name = '0'
            )
        else:
            return FileBrowserLinkFileGroupPermissionRequest(
        )
        """

    def testFileBrowserLinkFileGroupPermissionRequest(self):
        """Test FileBrowserLinkFileGroupPermissionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
