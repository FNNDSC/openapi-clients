# coding: utf-8

# flake8: noqa

"""
    ChRIS Research Integration System: Ultron BackEnd (CUBE) API

    The ChRIS Ultron BackEnd (CUBE) is the core backend API of ChRIS. It manages ChRIS users, plugins, pipelines, and the provenance of data analyses as ChRIS feeds.

    The version of the OpenAPI document: 0.0.0+unknown
    Contact: dev@babymri.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.1a1"

# import apis into sdk package
from aiochris_oag.api.auth_token_api import AuthTokenApi
from aiochris_oag.api.chris_admin_api import ChrisAdminApi
from aiochris_oag.api.chrisinstance_api import ChrisinstanceApi
from aiochris_oag.api.comments_api import CommentsApi
from aiochris_oag.api.computeresources_api import ComputeresourcesApi
from aiochris_oag.api.default_api import DefaultApi
from aiochris_oag.api.downloadtokens_api import DownloadtokensApi
from aiochris_oag.api.filebrowser_api import FilebrowserApi
from aiochris_oag.api.grouppermissions_api import GrouppermissionsApi
from aiochris_oag.api.groups_api import GroupsApi
from aiochris_oag.api.note_api import NoteApi
from aiochris_oag.api.pacs_api import PacsApi
from aiochris_oag.api.pipelines_api import PipelinesApi
from aiochris_oag.api.plugininstances_api import PlugininstancesApi
from aiochris_oag.api.plugins_api import PluginsApi
from aiochris_oag.api.publicfeeds_api import PublicfeedsApi
from aiochris_oag.api.schema_api import SchemaApi
from aiochris_oag.api.search_api import SearchApi
from aiochris_oag.api.taggings_api import TaggingsApi
from aiochris_oag.api.tags_api import TagsApi
from aiochris_oag.api.userfiles_api import UserfilesApi
from aiochris_oag.api.userpermissions_api import UserpermissionsApi
from aiochris_oag.api.users_api import UsersApi

# import ApiClient
from aiochris_oag.api_response import ApiResponse
from aiochris_oag.api_client import ApiClient
from aiochris_oag.configuration import Configuration
from aiochris_oag.exceptions import OpenApiException
from aiochris_oag.exceptions import ApiTypeError
from aiochris_oag.exceptions import ApiValueError
from aiochris_oag.exceptions import ApiKeyError
from aiochris_oag.exceptions import ApiAttributeError
from aiochris_oag.exceptions import ApiException

# import models into sdk package
from aiochris_oag.models.auth_token import AuthToken
from aiochris_oag.models.auth_token_request import AuthTokenRequest
from aiochris_oag.models.blank_enum import BlankEnum
from aiochris_oag.models.bool_parameter import BoolParameter
from aiochris_oag.models.chris_instance import ChrisInstance
from aiochris_oag.models.comment import Comment
from aiochris_oag.models.comment_request import CommentRequest
from aiochris_oag.models.compute_resource import ComputeResource
from aiochris_oag.models.compute_resource_request import ComputeResourceRequest
from aiochris_oag.models.default_piping_bool_parameter import DefaultPipingBoolParameter
from aiochris_oag.models.default_piping_bool_parameter_request import DefaultPipingBoolParameterRequest
from aiochris_oag.models.default_piping_float_parameter import DefaultPipingFloatParameter
from aiochris_oag.models.default_piping_float_parameter_request import DefaultPipingFloatParameterRequest
from aiochris_oag.models.default_piping_int_parameter import DefaultPipingIntParameter
from aiochris_oag.models.default_piping_int_parameter_request import DefaultPipingIntParameterRequest
from aiochris_oag.models.default_piping_str_parameter import DefaultPipingStrParameter
from aiochris_oag.models.default_piping_str_parameter_request import DefaultPipingStrParameterRequest
from aiochris_oag.models.feed import Feed
from aiochris_oag.models.feed_group_permission import FeedGroupPermission
from aiochris_oag.models.feed_group_permission_request import FeedGroupPermissionRequest
from aiochris_oag.models.feed_request import FeedRequest
from aiochris_oag.models.feed_user_permission import FeedUserPermission
from aiochris_oag.models.feed_user_permission_request import FeedUserPermissionRequest
from aiochris_oag.models.file_browser_file import FileBrowserFile
from aiochris_oag.models.file_browser_file_group_permission import FileBrowserFileGroupPermission
from aiochris_oag.models.file_browser_file_group_permission_request import FileBrowserFileGroupPermissionRequest
from aiochris_oag.models.file_browser_file_request import FileBrowserFileRequest
from aiochris_oag.models.file_browser_file_user_permission import FileBrowserFileUserPermission
from aiochris_oag.models.file_browser_file_user_permission_request import FileBrowserFileUserPermissionRequest
from aiochris_oag.models.file_browser_folder import FileBrowserFolder
from aiochris_oag.models.file_browser_folder_group_permission import FileBrowserFolderGroupPermission
from aiochris_oag.models.file_browser_folder_group_permission_request import FileBrowserFolderGroupPermissionRequest
from aiochris_oag.models.file_browser_folder_request import FileBrowserFolderRequest
from aiochris_oag.models.file_browser_folder_user_permission import FileBrowserFolderUserPermission
from aiochris_oag.models.file_browser_folder_user_permission_request import FileBrowserFolderUserPermissionRequest
from aiochris_oag.models.file_browser_link_file import FileBrowserLinkFile
from aiochris_oag.models.file_browser_link_file_group_permission import FileBrowserLinkFileGroupPermission
from aiochris_oag.models.file_browser_link_file_group_permission_request import FileBrowserLinkFileGroupPermissionRequest
from aiochris_oag.models.file_browser_link_file_request import FileBrowserLinkFileRequest
from aiochris_oag.models.file_browser_link_file_user_permission import FileBrowserLinkFileUserPermission
from aiochris_oag.models.file_browser_link_file_user_permission_request import FileBrowserLinkFileUserPermissionRequest
from aiochris_oag.models.file_download_token import FileDownloadToken
from aiochris_oag.models.file_download_token_request import FileDownloadTokenRequest
from aiochris_oag.models.float_parameter import FloatParameter
from aiochris_oag.models.ftype_enum import FtypeEnum
from aiochris_oag.models.generic_default_piping_parameter import GenericDefaultPipingParameter
from aiochris_oag.models.generic_default_piping_parameter_value import GenericDefaultPipingParameterValue
from aiochris_oag.models.generic_parameter import GenericParameter
from aiochris_oag.models.group import Group
from aiochris_oag.models.group_request import GroupRequest
from aiochris_oag.models.group_user import GroupUser
from aiochris_oag.models.group_user_request import GroupUserRequest
from aiochris_oag.models.int_parameter import IntParameter
from aiochris_oag.models.note import Note
from aiochris_oag.models.note_request import NoteRequest
from aiochris_oag.models.pacs_file import PACSFile
from aiochris_oag.models.pacs_series import PACSSeries
from aiochris_oag.models.pacs_series_patient_sex import PACSSeriesPatientSex
from aiochris_oag.models.paginated_comment_list import PaginatedCommentList
from aiochris_oag.models.paginated_compute_resource_list import PaginatedComputeResourceList
from aiochris_oag.models.paginated_feed_group_permission_list import PaginatedFeedGroupPermissionList
from aiochris_oag.models.paginated_feed_list import PaginatedFeedList
from aiochris_oag.models.paginated_feed_user_permission_list import PaginatedFeedUserPermissionList
from aiochris_oag.models.paginated_file_browser_file_group_permission_list import PaginatedFileBrowserFileGroupPermissionList
from aiochris_oag.models.paginated_file_browser_file_list import PaginatedFileBrowserFileList
from aiochris_oag.models.paginated_file_browser_file_user_permission_list import PaginatedFileBrowserFileUserPermissionList
from aiochris_oag.models.paginated_file_browser_folder_group_permission_list import PaginatedFileBrowserFolderGroupPermissionList
from aiochris_oag.models.paginated_file_browser_folder_list import PaginatedFileBrowserFolderList
from aiochris_oag.models.paginated_file_browser_folder_user_permission_list import PaginatedFileBrowserFolderUserPermissionList
from aiochris_oag.models.paginated_file_browser_link_file_group_permission_list import PaginatedFileBrowserLinkFileGroupPermissionList
from aiochris_oag.models.paginated_file_browser_link_file_list import PaginatedFileBrowserLinkFileList
from aiochris_oag.models.paginated_file_browser_link_file_user_permission_list import PaginatedFileBrowserLinkFileUserPermissionList
from aiochris_oag.models.paginated_file_download_token_list import PaginatedFileDownloadTokenList
from aiochris_oag.models.paginated_generic_default_piping_parameter_list import PaginatedGenericDefaultPipingParameterList
from aiochris_oag.models.paginated_generic_parameter_list import PaginatedGenericParameterList
from aiochris_oag.models.paginated_group_list import PaginatedGroupList
from aiochris_oag.models.paginated_group_user_list import PaginatedGroupUserList
from aiochris_oag.models.paginated_pacs_file_list import PaginatedPACSFileList
from aiochris_oag.models.paginated_pacs_series_list import PaginatedPACSSeriesList
from aiochris_oag.models.paginated_pipeline_list import PaginatedPipelineList
from aiochris_oag.models.paginated_pipeline_source_file_list import PaginatedPipelineSourceFileList
from aiochris_oag.models.paginated_plugin_admin_list import PaginatedPluginAdminList
from aiochris_oag.models.paginated_plugin_instance_list import PaginatedPluginInstanceList
from aiochris_oag.models.paginated_plugin_instance_split_list import PaginatedPluginInstanceSplitList
from aiochris_oag.models.paginated_plugin_list import PaginatedPluginList
from aiochris_oag.models.paginated_plugin_meta_list import PaginatedPluginMetaList
from aiochris_oag.models.paginated_plugin_parameter_list import PaginatedPluginParameterList
from aiochris_oag.models.paginated_plugin_piping_list import PaginatedPluginPipingList
from aiochris_oag.models.paginated_tag_list import PaginatedTagList
from aiochris_oag.models.paginated_tagging_list import PaginatedTaggingList
from aiochris_oag.models.paginated_user_file_list import PaginatedUserFileList
from aiochris_oag.models.paginated_user_list import PaginatedUserList
from aiochris_oag.models.paginated_workflow_list import PaginatedWorkflowList
from aiochris_oag.models.path_parameter import PathParameter
from aiochris_oag.models.patient_sex_enum import PatientSexEnum
from aiochris_oag.models.permission_enum import PermissionEnum
from aiochris_oag.models.pipeline import Pipeline
from aiochris_oag.models.pipeline_custom_json import PipelineCustomJson
from aiochris_oag.models.pipeline_request import PipelineRequest
from aiochris_oag.models.pipeline_source_file import PipelineSourceFile
from aiochris_oag.models.pipeline_source_file_ftype import PipelineSourceFileFtype
from aiochris_oag.models.pipeline_source_file_request import PipelineSourceFileRequest
from aiochris_oag.models.plugin import Plugin
from aiochris_oag.models.plugin_admin import PluginAdmin
from aiochris_oag.models.plugin_admin_request import PluginAdminRequest
from aiochris_oag.models.plugin_instance import PluginInstance
from aiochris_oag.models.plugin_instance_request import PluginInstanceRequest
from aiochris_oag.models.plugin_instance_split import PluginInstanceSplit
from aiochris_oag.models.plugin_instance_split_request import PluginInstanceSplitRequest
from aiochris_oag.models.plugin_meta import PluginMeta
from aiochris_oag.models.plugin_parameter import PluginParameter
from aiochris_oag.models.plugin_parameter_default import PluginParameterDefault
from aiochris_oag.models.plugin_parameter_type import PluginParameterType
from aiochris_oag.models.plugin_piping import PluginPiping
from aiochris_oag.models.plugin_type import PluginType
from aiochris_oag.models.status_enum import StatusEnum
from aiochris_oag.models.str_parameter import StrParameter
from aiochris_oag.models.tag import Tag
from aiochris_oag.models.tag_request import TagRequest
from aiochris_oag.models.tagging import Tagging
from aiochris_oag.models.unextpath_parameter import UnextpathParameter
from aiochris_oag.models.user import User
from aiochris_oag.models.user_file import UserFile
from aiochris_oag.models.user_file_request import UserFileRequest
from aiochris_oag.models.user_request import UserRequest
from aiochris_oag.models.workflow import Workflow
from aiochris_oag.models.workflow_request import WorkflowRequest
