"""Contact constants."""

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import Platform

PLATFORMS: list[Platform] = []
DOMAIN = "ms365_contacts"

ATTR_EMAIL = "email"
ATTR_GIVEN_NAME = "given_name"
ATTR_SURNAME = "surname"

PERM_CONTACTS_READ = "Contacts.Read"

CONTACTS_SEARCH_SCHEMA = vol.Schema(
    {
        vol.Optional(ATTR_GIVEN_NAME): cv.string,
        vol.Optional(ATTR_SURNAME): cv.string,
        vol.Optional(ATTR_EMAIL): cv.string,
    }
)
