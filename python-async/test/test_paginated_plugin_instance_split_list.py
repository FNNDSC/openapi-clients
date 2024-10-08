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

from aiochris_oag.models.paginated_plugin_instance_split_list import PaginatedPluginInstanceSplitList

class TestPaginatedPluginInstanceSplitList(unittest.TestCase):
    """PaginatedPluginInstanceSplitList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPluginInstanceSplitList:
        """Test PaginatedPluginInstanceSplitList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPluginInstanceSplitList`
        """
        model = PaginatedPluginInstanceSplitList()
        if include_optional:
            return PaginatedPluginInstanceSplitList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    aiochris_oag.models.plugin_instance_split.PluginInstanceSplit(
                        url = '', 
                        id = 56, 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        filter = '', 
                        plugin_inst_id = 56, 
                        created_plugin_inst_ids = '', 
                        plugin_inst = '', )
                    ]
            )
        else:
            return PaginatedPluginInstanceSplitList(
        )
        """

    def testPaginatedPluginInstanceSplitList(self):
        """Test PaginatedPluginInstanceSplitList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
