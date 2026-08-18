"""Schema for MS365 Integration."""

import voluptuous as vol

import homeassistant.helpers.config_validation as cv

from ..const import CONF_SHARED_MAILBOX

CONFIG_SCHEMA_INTEGRATION = {
    vol.Optional(CONF_SHARED_MAILBOX, default=""): cv.string,
}
