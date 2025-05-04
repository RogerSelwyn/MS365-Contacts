"""Do configuration setup."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, SupportsResponse

from .const_integration import CONTACTS_SEARCH_SCHEMA, DOMAIN, PLATFORMS
from .services_integration import ContactServices

_LOGGER = logging.getLogger(__name__)


async def async_do_setup(hass: HomeAssistant, entry: ConfigEntry, account):  # pylint: disable=unused-argument
    """Run the setup after we have everything configured."""

    _LOGGER.debug("Contacts setup - start")
    services = ContactServices(hass, account)

    hass.services.async_register(
        DOMAIN,
        "contacts_search",
        services.async_contacts_search,
        CONTACTS_SEARCH_SCHEMA,
        SupportsResponse.ONLY,
    )

    _LOGGER.debug("Contacts setup - finish")
    return None, None, PLATFORMS
