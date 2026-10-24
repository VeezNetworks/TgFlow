from ...tl import types as _tp


ContactsNotModified = getattr(_tp, 'ContactsContactsNotModified', getattr(_tp, 'ContactsNotModified', None))
ContactsContactsNotModified = getattr(_tp, 'ContactsContactsNotModified', None)
Contacts = getattr(_tp, 'ContactsContacts', getattr(_tp, 'Contacts', None))
ContactsContacts = getattr(_tp, 'ContactsContacts', None)
ImportedContacts = getattr(_tp, 'ContactsImportedContacts', getattr(_tp, 'ImportedContacts', None))
ContactsImportedContacts = getattr(_tp, 'ContactsImportedContacts', None)
Blocked = getattr(_tp, 'ContactsBlocked', getattr(_tp, 'Blocked', None))
ContactsBlocked = getattr(_tp, 'ContactsBlocked', None)
BlockedSlice = getattr(_tp, 'ContactsBlockedSlice', getattr(_tp, 'BlockedSlice', None))
ContactsBlockedSlice = getattr(_tp, 'ContactsBlockedSlice', None)
Found = getattr(_tp, 'ContactsFound', getattr(_tp, 'Found', None))
ContactsFound = getattr(_tp, 'ContactsFound', None)
ResolvedPeer = getattr(_tp, 'ContactsResolvedPeer', getattr(_tp, 'ResolvedPeer', None))
ContactsResolvedPeer = getattr(_tp, 'ContactsResolvedPeer', None)
TopPeersNotModified = getattr(_tp, 'ContactsTopPeersNotModified', getattr(_tp, 'TopPeersNotModified', None))
ContactsTopPeersNotModified = getattr(_tp, 'ContactsTopPeersNotModified', None)
TopPeers = getattr(_tp, 'ContactsTopPeers', getattr(_tp, 'TopPeers', None))
ContactsTopPeers = getattr(_tp, 'ContactsTopPeers', None)
TopPeersDisabled = getattr(_tp, 'ContactsTopPeersDisabled', getattr(_tp, 'TopPeersDisabled', None))
ContactsTopPeersDisabled = getattr(_tp, 'ContactsTopPeersDisabled', None)
ContactBirthdays = getattr(_tp, 'ContactsContactBirthdays', getattr(_tp, 'ContactBirthdays', None))
ContactsContactBirthdays = getattr(_tp, 'ContactsContactBirthdays', None)
SponsoredPeersEmpty = getattr(_tp, 'ContactsSponsoredPeersEmpty', getattr(_tp, 'SponsoredPeersEmpty', None))
ContactsSponsoredPeersEmpty = getattr(_tp, 'ContactsSponsoredPeersEmpty', None)
SponsoredPeers = getattr(_tp, 'ContactsSponsoredPeers', getattr(_tp, 'SponsoredPeers', None))
ContactsSponsoredPeers = getattr(_tp, 'ContactsSponsoredPeers', None)

__all__ = [
    "ContactsNotModified",
    "ContactsContactsNotModified",
    "Contacts",
    "ContactsContacts",
    "ImportedContacts",
    "ContactsImportedContacts",
    "Blocked",
    "ContactsBlocked",
    "BlockedSlice",
    "ContactsBlockedSlice",
    "Found",
    "ContactsFound",
    "ResolvedPeer",
    "ContactsResolvedPeer",
    "TopPeersNotModified",
    "ContactsTopPeersNotModified",
    "TopPeers",
    "ContactsTopPeers",
    "TopPeersDisabled",
    "ContactsTopPeersDisabled",
    "ContactBirthdays",
    "ContactsContactBirthdays",
    "SponsoredPeersEmpty",
    "ContactsSponsoredPeersEmpty",
    "SponsoredPeers",
    "ContactsSponsoredPeers"
]
