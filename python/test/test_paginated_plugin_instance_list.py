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

from chris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList

class TestPaginatedPluginInstanceList(unittest.TestCase):
    """PaginatedPluginInstanceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedPluginInstanceList:
        """Test PaginatedPluginInstanceList
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedPluginInstanceList`
        """
        model = PaginatedPluginInstanceList()
        if include_optional:
            return PaginatedPluginInstanceList(
                count = 123,
                next = 'http://api.example.org/accounts/?offset=400&limit=100',
                previous = 'http://api.example.org/accounts/?offset=200&limit=100',
                results = [
                    chris_oag.models.plugin_instance.PluginInstance(
                        url = '', 
                        id = 56, 
                        title = '', 
                        previous_id = 56, 
                        compute_resource_name = '', 
                        plugin_id = 56, 
                        plugin_name = '', 
                        plugin_version = '', 
                        plugin_type = null, 
                        feed_id = 56, 
                        start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        output_path = '', 
                        status = 'created', 
                        pipeline_id = 56, 
                        pipeline_name = '', 
                        workflow_id = 56, 
                        summary = '', 
                        raw = '', 
                        owner_username = '', 
                        cpu_limit = 56, 
                        memory_limit = 56, 
                        number_of_workers = -2147483648, 
                        gpu_limit = -2147483648, 
                        size = -9223372036854775808, 
                        error_code = '', 
                        output_folder = '', 
                        previous = '', 
                        feed = '', 
                        plugin = '', 
                        workflow = '', 
                        compute_resource = '', 
                        descendants = '', 
                        parameters = '', 
                        splits = '', )
                    ]
            )
        else:
            return PaginatedPluginInstanceList(
        )
        """

    def testPaginatedPluginInstanceList(self):
        """Test PaginatedPluginInstanceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
