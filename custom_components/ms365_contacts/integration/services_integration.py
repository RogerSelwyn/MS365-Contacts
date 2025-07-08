"""Services for the contacts integration"""

import functools as ft

# import json
from dataclasses import dataclass, field
from typing import Any

from homeassistant.core import HomeAssistant, ServiceCall
from O365.address_book import (  # pylint: disable=no-name-in-module, import-error
    AddressBook,
    Contact,
)
from O365.utils.query import (  # pylint: disable=no-name-in-module, import-error
    QueryBuilder,
)

from .const_integration import ATTR_EMAIL, ATTR_GIVEN_NAME, ATTR_SURNAME


class ContactServices:
    """Contact services."""

    def __init__(self, hass: HomeAssistant, account):
        """Initialise the contact services."""
        self._hass = hass
        self._address_book: AddressBook = account.address_book()
        self._builder = QueryBuilder(protocol=account.protocol)

    async def async_contacts_search(self, call: ServiceCall):  # pylint: disable=unused-argument
        """Search for contacts"""
        query = self._builder.select()
        query = self._add_to_query(call.data, query, ATTR_GIVEN_NAME, "givenName")
        query = self._add_to_query(call.data, query, ATTR_SURNAME, "surname")
        if email := call.data.get(ATTR_EMAIL, None):
            query = query & self._builder.any(
                collection="emailAddresses",
                filter_instance=self._builder.equals("address", email),
            )

        contacts = await self._hass.async_add_executor_job(
            ft.partial(self._address_book.get_contacts, query=query)
        )
        return {"contacts": [MS365Contact(contact) for contact in contacts]}

    def _add_to_query(self, data, query: QueryBuilder, ms365attr, msattr):
        if attribute := data.get(ms365attr, None):
            query = query & self._builder.contains(msattr, attribute)
        return query


@dataclass
class MS365Contact:
    """A Contact to return to the service."""

    contact: Any = field(init=True, repr=False)
    given_name: str = field(init=False, repr=True)
    surname: str = field(init=False, repr=True)
    title: str = field(init=False, repr=True)
    display_name: str = field(init=False, repr=True)
    file_as: str = field(init=False, repr=True)
    main_email: str = field(init=False, repr=True)
    emails: list[str] = field(init=False, repr=True)
    mobile_phone: str = field(init=False, repr=True)
    home_phones: list[str] = field(init=False, repr=True)
    home_address: dict = field(init=False, repr=True)
    business_phones: list[str] = field(init=False, repr=True)
    business_address: dict = field(init=False, repr=True)
    office_location: str = field(init=False, repr=True)
    job_title: str = field(init=False, repr=True)
    other_address: dict = field(init=False, repr=True)
    preferred_language: str = field(init=False, repr=True)
    personal_notes: str = field(init=False, repr=True)

    def __init__(self, contact: Contact):
        self.given_name = contact.name
        self.surname = contact.surname
        self.title = contact.title
        self.display_name = contact.display_name
        self.file_as = contact.fileAs
        self.main_email = contact.main_email
        self.emails = [email.address for email in contact.emails]
        self.mobile_phone = contact.mobile_phone
        self.home_phones = list(contact.home_phones)
        self.home_address = contact.home_address
        self.business_phones = list(contact.business_phones)
        self.business_address = contact.business_address
        self.office_location = contact.office_location
        self.job_title = contact.job_title
        self.other_address = contact.other_address
        self.preferred_language = contact.preferred_language
        self.personal_notes = contact.personal_notes
