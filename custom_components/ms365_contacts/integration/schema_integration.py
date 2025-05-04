"""Schema for MS365 Integration."""

import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from ..const import (
    CONF_SHARED_MAILBOX,
)

CONFIG_SCHEMA_INTEGRATION = {
    vol.Optional(CONF_SHARED_MAILBOX, default=""): cv.string,
}
