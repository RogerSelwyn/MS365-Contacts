"""Configuration flow for the skyq platform."""

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant import (
    config_entries,
)
from homeassistant.data_entry_flow import FlowResult

from ..classes.config_entry import MS365ConfigEntry
from ..const import CONF_SHARED_MAILBOX


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


async def async_integration_imports(hass, import_data):  # pylint: disable=unused-argument
    """Do the integration  level import tasks."""
    # This is used for migration from O365 which is not relevant for Contacts
    return


class MS365OptionsFlowHandler(config_entries.OptionsFlow):
    """Config flow options for MS365."""

    def __init__(self, entry: MS365ConfigEntry):
        """Initialize MS365 options flow."""

    async def async_step_init(
        self,
        user_input=None,  # pylint: disable=unused-argument
    ) -> FlowResult:
        """Set up the option flow."""

        return await self.async_step_user()

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Handle a flow initialized by the user."""

        return self.async_create_entry(title="", data=user_input)
