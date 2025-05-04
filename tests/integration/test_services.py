# pylint: disable=unused-argument,line-too-long,wrong-import-order
"""Test service usage."""

import pytest

from homeassistant.core import HomeAssistant

from requests_mock import Mocker


from ..conftest import MS365MockConfigEntry

from .const_integration import DOMAIN
from .helpers_integration.mocks import MS365MOCKS


async def test_base_service_setup(
    hass: HomeAssistant,
    setup_base_integration,
    base_config_entry: MS365MockConfigEntry,
) -> None:
    """Test the reconfigure flow."""
    assert hass.services.has_service(DOMAIN, "contacts_search")


async def test_contact_search(
    hass: HomeAssistant,
    setup_base_integration,
) -> None:
    """Test contact search."""

    given_name = "Roger"
    email = "roger.blggs@nospam.com"
    response = await hass.services.async_call(
        DOMAIN,
        "contacts_search",
        {"given_name": given_name, "email": email},
        blocking=True,
        return_response=True,
    )
    await hass.async_block_till_done()
    assert len(response["contacts"]) == 2
    assert response["contacts"][0].given_name == given_name


@pytest.mark.parametrize(
    "base_config_entry",
    [{"shared_mailbox": "jane.doe@nomail.com"}],
    indirect=True,
)
@pytest.mark.parametrize("base_token", ["Contacts.Read.Shared"], indirect=True)
async def test_shared_contact_search(
    hass: HomeAssistant,
    requests_mock: Mocker,
    setup_base_integration,
    base_config_entry: MS365MockConfigEntry,
) -> None:
    """Test shared contact search."""
    MS365MOCKS.shared_mocks(requests_mock)
    given_name = "Roger"
    response = await hass.services.async_call(
        DOMAIN,
        "contacts_search",
        {
            "given_name": given_name,
        },
        blocking=True,
        return_response=True,
    )
    await hass.async_block_till_done()
    assert len(response["contacts"]) == 2
    assert response["contacts"][0].given_name == given_name
