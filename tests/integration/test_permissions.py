# pylint: disable=unused-argument, line-too-long
"""Test permission handling."""

from unittest.mock import patch

import pytest

from homeassistant.core import HomeAssistant

from ..helpers.mock_config_entry import MS365MockConfigEntry
from ..helpers.utils import build_token_file


async def test_base_permissions(
    hass: HomeAssistant,
    setup_base_integration,
    base_config_entry: MS365MockConfigEntry,
) -> None:
    """Test base permissions."""
    assert "Contacts.Read" in base_config_entry.runtime_data.permissions.permissions


@pytest.mark.parametrize(
    "base_config_entry",
    [{"shared_mailbox": "jane.doe@nomail.com"}],
    indirect=True,
)
@pytest.mark.parametrize("base_token", ["Contacts.Read.Shared"], indirect=True)
async def test_shared_permissions(
    hass: HomeAssistant,
    setup_base_integration,
    base_config_entry: MS365MockConfigEntry,
) -> None:
    """Test shared permissions."""
    assert (
        "Contacts.Read.Shared" in base_config_entry.runtime_data.permissions.permissions
    )


async def test_missing_permissions(
    tmp_path,
    hass: HomeAssistant,
    base_config_entry: MS365MockConfigEntry,
    caplog: pytest.LogCaptureFixture,
):
    """Test for missing permissions."""
    build_token_file(tmp_path, "")

    base_config_entry.add_to_hass(hass)
    with patch(
        "homeassistant.helpers.issue_registry.async_create_issue"
    ) as mock_async_create_issue:
        await hass.config_entries.async_setup(base_config_entry.entry_id)

    assert "Minimum required permissions: 'Contacts.Read'" in caplog.text
    assert mock_async_create_issue.called
