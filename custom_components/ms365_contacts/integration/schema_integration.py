"""Schema for MS365 Integration."""

import probatio

import homeassistant.helpers.config_validation as cv

from ..const import CONF_SHARED_MAILBOX

CONFIG_SCHEMA_INTEGRATION = {
    probatio.Optional(CONF_SHARED_MAILBOX, default=""): cv.string,
}
