---
title: Installation and Configuration
nav_order: 4
---

# Installation and Configuration
This page details the configuration details for this integration. General instructions can be found on the MS365 Home Assistant [Installation and Configuration](https://rogerselwyn.github.io/MS365-HomeAssistant/installation_and_configuration.html) page.

1. Navigate to the Integrations section
1. Add this repository as a Custom Repository (Integration) via the menu at top right.
1. Search for "Microsoft 365 To Do"
1. Select "Install this repository"
1. Restart Home Assistant
1. Go to the Home Assistant Devices configuration page
1. Click "Add Integration"
1. Search for "Microsoft 365 Contacts"
1. Click on the result, and follow the prompts.


### Configuration variables

Key | Type | Required | Description
-- | -- | -- | --
`entity_name` | `string` | `True` | Uniquely identifying name for the account. Do not use email address or spaces.
`client_id` | `string` | `True` | Client ID from your Entra ID App Registration.
`client_secret` | `string` | `True` | Client Secret from your Entra ID App Registration.
`alt_auth_method` | `boolean` | `False` | If False (default), authentication is not dependent on internet access to your HA instance. [See Authentication](./authentication.md)
`shared_mailbox` | `string` | `False` | Email address or ID of shared mailbox (This should not be the same email address as the loggin in user).

#### Advanced API Options

These options will only be relevant for users in very specific circumstances.

Key | Type | Required | Description
-- | -- | -- | --
`country` | `string` | `True` | Selection of an alternate country specific API. Currently only 21Vianet from China.
`tenant_id` | `string` | `False` | Azure tenant ID for single-tenant app registrations. Leave blank for multi-tenant apps.