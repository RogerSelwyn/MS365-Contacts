"""Mock setup."""

from ...helpers.utils import mock_call
from ..const_integration import CN21VURL, URL


class MS365Mocks:
    """Standard mocks."""

    def standard_mocks(self, requests_mock):
        """Setup the standard mocks."""
        mock_call(requests_mock, URL.OPENID, "openid")
        mock_call(requests_mock, URL.ME, "me")
        mock_call(requests_mock, URL.CONTACTS, "contacts")

    def cn21v_mocks(self, requests_mock):
        """Setup the standard mocks."""
        mock_call(requests_mock, CN21VURL.DISCOVERY, "discovery")
        mock_call(requests_mock, CN21VURL.OPENID, "openid")
        mock_call(requests_mock, CN21VURL.ME, "me")
        mock_call(requests_mock, CN21VURL.CONTACTS, "contacts")

    def shared_mocks(self, requests_mock):
        """Setup the standard mocks."""
        mock_call(requests_mock, URL.OPENID, "openid")
        mock_call(requests_mock, URL.ME, "me")
        mock_call(requests_mock, URL.SHARED_CONTACTS, "contacts")


MS365MOCKS = MS365Mocks()


def _generic_mocks(requests_mock):
    mock_call(requests_mock, URL.OPENID, "openid")
    mock_call(requests_mock, URL.ME, "me")
    mock_call(requests_mock, URL.CONTACTS, "contacts")
