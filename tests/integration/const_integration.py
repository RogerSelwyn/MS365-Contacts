# pylint: disable=unused-import
"""Constants for contacts integration."""

from copy import deepcopy
from enum import Enum

from custom_components.ms365_contacts.config_flow import MS365ConfigFlow  # noqa: F401
from custom_components.ms365_contacts.const import (  # noqa: F401
    AUTH_CALLBACK_PATH_ALT,
    COUNTRY_URLS,
    OAUTH_REDIRECT_URL,
    CountryOptions,
)
from custom_components.ms365_contacts.integration.const_integration import (
    DOMAIN,  # noqa: F401
)

from ..const import CLIENT_ID, CLIENT_SECRET, ENTITY_NAME

AUTH_CALLBACK_PATH_DEFAULT = COUNTRY_URLS[CountryOptions.DEFAULT][OAUTH_REDIRECT_URL]
BASE_CONFIG_ENTRY = {
    "entity_name": ENTITY_NAME,
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "alt_auth_method": False,
    "shared_mailbox": "",
    "api_options": {"country": "Default"},
}
BASE_TOKEN_PERMS = "Contacts.Read"
BASE_MISSING_PERMS = BASE_TOKEN_PERMS
SHARED_TOKEN_PERMS = "Contacts.Read.Shared"
UPDATE_TOKEN_PERMS = None
UPDATE_OPTIONS = None

ALT_CONFIG_ENTRY = deepcopy(BASE_CONFIG_ENTRY)
ALT_CONFIG_ENTRY["alt_auth_method"] = True
COUNTRY_CONFIG_ENTRY = deepcopy(BASE_CONFIG_ENTRY)
COUNTRY_CONFIG_ENTRY["api_options"]["country"] = "21Vianet (China)"

RECONFIGURE_CONFIG_ENTRY = deepcopy(BASE_CONFIG_ENTRY)
del RECONFIGURE_CONFIG_ENTRY["entity_name"]

MIGRATION_CONFIG_ENTRY = {
    "data": BASE_CONFIG_ENTRY,
    "options": {},
}

DIAGNOSTIC_GRANTED_PERMISSIONS = [
    "Contacts.Read",
    "User.Read",
    "email",
    "openid",
    "profile",
]
DIAGNOSTIC_REQUESTED_PERMISSIONS = [
    "User.Read",
    "Contacts.Read",
]

FULL_INIT_ENTITY_NO = 0


class URL(Enum):
    """List of URLs"""

    OPENID = (
        "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration"
    )
    ME = "https://graph.microsoft.com/v1.0/me"
    CONTACTS = "https://graph.microsoft.com/v1.0/me/contacts"
    SHARED_CONTACTS = (
        "https://graph.microsoft.com/v1.0/users/jane.doe@nomail.com/contacts"
    )


class CN21VURL(Enum):
    """List of URLs"""

    DISCOVERY = "https://login.microsoftonline.com/common/discovery/instance"
    OPENID = "https://login.partner.microsoftonline.cn/common/v2.0/.well-known/openid-configuration"
    ME = "https://microsoftgraph.chinacloudapi.cn/v1.0/me"
    CONTACTS = "https://microsoftgraph.chinacloudapi.cn/v1.0/me/contacts"
