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

from aiochris_oag.models.paginated_plugin_piping_list import PaginatedPluginPipingList

class TestPaginatedPluginPipingList(unittest.TestCase):
    """PaginatedPluginPipingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPluginPipingList:
        """Test PaginatedPluginPipingList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPluginPipingList`
        """
        model = PaginatedPluginPipingList()
        if include_optional:
            return PaginatedPluginPipingList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    aiochris_oag.models.plugin_piping.PluginPiping(
                        url = '', 
                        id = 56, 
                        previous_id = 56, 
                        title = '', 
                        plugin_id = 56, 
                        plugin_name = '', 
                        plugin_version = '', 
                        pipeline_id = 56, 
                        previous = '', 
                        plugin = '', 
                        pipeline = '', )
                    ]
            )
        else:
            return PaginatedPluginPipingList(
        )
        """

    def testPaginatedPluginPipingList(self):
        """Test PaginatedPluginPipingList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
