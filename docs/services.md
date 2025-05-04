---
title: Services
nav_order: 15
---

# Services

##  Contacts Services
### ms365_contacts.contacts_search
Searches for contacts using the provided parameters - All parameters are shown in the available parameter list on the Developer Tools/Services tab.

#### Example create event service call

```yaml
action: ms365_contacts.contacts_search
data:
  given_name: Joe
  surname: Bloggs
  email: joe.bloggs@nospam.com
```

