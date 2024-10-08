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

from chris_oag.models.paginated_file_browser_folder_list import PaginatedFileBrowserFolderList

class TestPaginatedFileBrowserFolderList(unittest.TestCase):
    """PaginatedFileBrowserFolderList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedFileBrowserFolderList:
        """Test PaginatedFileBrowserFolderList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedFileBrowserFolderList`
        """
        model = PaginatedFileBrowserFolderList()
        if include_optional:
            return PaginatedFileBrowserFolderList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    chris_oag.models.file_browser_folder.FileBrowserFolder(
                        url = '', 
                        id = 56, 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        path = '', 
                        public = True, 
                        owner_username = '', 
                        parent = '', 
                        children = '', 
                        files = '', 
                        link_files = '', 
                        group_permissions = '', 
                        user_permissions = '', 
                        owner = '', )
                    ]
            )
        else:
            return PaginatedFileBrowserFolderList(
        )
        """

    def testPaginatedFileBrowserFolderList(self):
        """Test PaginatedFileBrowserFolderList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
