"""Configuration flow for the skyq platform."""

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlowResult
import homeassistant.helpers.config_validation as cv

from ..classes.config_entry import MS365ConfigEntry
from ..const import CONF_SHARED_MAILBOX

INTEGRATION_CONFIG_VERSION = 2
INRTEGRATION_CONFIG_MINOR_VERSION = 0


def integration_reconfigure_schema(entry_data):
    """Extend the schema with integration specific attributes."""
    return {
        vol.Optional(
            CONF_SHARED_MAILBOX,
            description={"suggested_value": entry_data.get(CONF_SHARED_MAILBOX, None)},
        ): cv.string,
    }


def integration_validate_schema(user_input):  # pylint: disable=unused-argument
    """Validate the user input."""
    return {}


class MS365OptionsFlowHandler(config_entries.OptionsFlow):
    """Config flow options for MS365."""

    def __init__(self, entry: MS365ConfigEntry) -> None:
        """Initialize MS365 options flow."""

    async def async_step_init(
        self,
        user_input=None,  # pylint: disable=unused-argument
    ) -> ConfigFlowResult:
        """Set up the option flow."""

        return self.async_abort(reason="no_options")
