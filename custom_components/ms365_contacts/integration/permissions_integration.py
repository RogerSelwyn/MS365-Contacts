"""Permissions processes for mail."""

from copy import deepcopy

from ..classes.permissions import BasePermissions
from ..const import (
    CONF_SHARED_MAILBOX,
    PERM_BASE_PERMISSIONS,
    PERM_SHARED,
)
from .const_integration import (
    PERM_CONTACTS_READ,
)


class Permissions(BasePermissions):
    """Class in support of building permission sets."""

    def __init__(self, hass, config, token_backend):
        """Initialise the class."""
        super().__init__(hass, config, token_backend)

        self._shared = PERM_SHARED if config.get(CONF_SHARED_MAILBOX) else ""

    @property
    def requested_permissions(self):
        """Return the required scope."""
        if not self._requested_permissions:
            self._requested_permissions = deepcopy(PERM_BASE_PERMISSIONS)
            self._build_contact_permissions()

        return self._requested_permissions

    def _build_contact_permissions(self):
        self._requested_permissions.append(PERM_CONTACTS_READ + self._shared)
