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

from chris_oag.models.feed import Feed

class TestFeed(unittest.TestCase):
    """Feed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Feed:
        """Test Feed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Feed`
        """
        model = Feed()
        if include_optional:
            return Feed(
                url = '',
                id = 56,
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                public = True,
                owner_username = '',
                folder_path = '',
                created_jobs = 56,
                waiting_jobs = 56,
                scheduled_jobs = 56,
                started_jobs = 56,
                registering_jobs = 56,
                finished_jobs = 56,
                errored_jobs = 56,
                cancelled_jobs = 56,
                folder = '',
                note = '',
                group_permissions = '',
                user_permissions = '',
                tags = '',
                taggings = '',
                comments = '',
                plugin_instances = '',
                owner = ''
            )
        else:
            return Feed(
                url = '',
                id = 56,
                creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner_username = '',
                folder_path = '',
                created_jobs = 56,
                waiting_jobs = 56,
                scheduled_jobs = 56,
                started_jobs = 56,
                registering_jobs = 56,
                finished_jobs = 56,
                errored_jobs = 56,
                cancelled_jobs = 56,
                folder = '',
                note = '',
                group_permissions = '',
                user_permissions = '',
                tags = '',
                taggings = '',
                comments = '',
                plugin_instances = '',
                owner = '',
        )
        """

    def testFeed(self):
        """Test Feed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
