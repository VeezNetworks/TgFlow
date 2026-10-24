from ...tl import functions as _fn


GetContactIDs = getattr(_fn, 'GetContactIDs', getattr(_fn, 'ContactsGetContactIDs', None))
ContactsGetContactIDs = getattr(_fn, 'ContactsGetContactIDs', None)
GetStatuses = getattr(_fn, 'GetStatuses', getattr(_fn, 'ContactsGetStatuses', None))
ContactsGetStatuses = getattr(_fn, 'ContactsGetStatuses', None)
GetContacts = getattr(_fn, 'GetContacts', getattr(_fn, 'ContactsGetContacts', None))
ContactsGetContacts = getattr(_fn, 'ContactsGetContacts', None)
ImportContacts = getattr(_fn, 'ImportContacts', getattr(_fn, 'ContactsImportContacts', None))
ContactsImportContacts = getattr(_fn, 'ContactsImportContacts', None)
DeleteContacts = getattr(_fn, 'DeleteContacts', getattr(_fn, 'ContactsDeleteContacts', None))
ContactsDeleteContacts = getattr(_fn, 'ContactsDeleteContacts', None)
DeleteByPhones = getattr(_fn, 'DeleteByPhones', getattr(_fn, 'ContactsDeleteByPhones', None))
ContactsDeleteByPhones = getattr(_fn, 'ContactsDeleteByPhones', None)
Block = getattr(_fn, 'Block', getattr(_fn, 'ContactsBlock', None))
ContactsBlock = getattr(_fn, 'ContactsBlock', None)
Unblock = getattr(_fn, 'Unblock', getattr(_fn, 'ContactsUnblock', None))
ContactsUnblock = getattr(_fn, 'ContactsUnblock', None)
GetBlocked = getattr(_fn, 'GetBlocked', getattr(_fn, 'ContactsGetBlocked', None))
ContactsGetBlocked = getattr(_fn, 'ContactsGetBlocked', None)
Search = getattr(_fn, 'Search', getattr(_fn, 'ContactsSearch', None))
ContactsSearch = getattr(_fn, 'ContactsSearch', None)
ResolveUsername = getattr(_fn, 'ResolveUsername', getattr(_fn, 'ContactsResolveUsername', None))
ContactsResolveUsername = getattr(_fn, 'ContactsResolveUsername', None)
GetTopPeers = getattr(_fn, 'GetTopPeers', getattr(_fn, 'ContactsGetTopPeers', None))
ContactsGetTopPeers = getattr(_fn, 'ContactsGetTopPeers', None)
ResetTopPeerRating = getattr(_fn, 'ResetTopPeerRating', getattr(_fn, 'ContactsResetTopPeerRating', None))
ContactsResetTopPeerRating = getattr(_fn, 'ContactsResetTopPeerRating', None)
ResetSaved = getattr(_fn, 'ResetSaved', getattr(_fn, 'ContactsResetSaved', None))
ContactsResetSaved = getattr(_fn, 'ContactsResetSaved', None)
GetSaved = getattr(_fn, 'GetSaved', getattr(_fn, 'ContactsGetSaved', None))
ContactsGetSaved = getattr(_fn, 'ContactsGetSaved', None)
ToggleTopPeers = getattr(_fn, 'ToggleTopPeers', getattr(_fn, 'ContactsToggleTopPeers', None))
ContactsToggleTopPeers = getattr(_fn, 'ContactsToggleTopPeers', None)
AddContact = getattr(_fn, 'AddContact', getattr(_fn, 'ContactsAddContact', None))
ContactsAddContact = getattr(_fn, 'ContactsAddContact', None)
AcceptContact = getattr(_fn, 'AcceptContact', getattr(_fn, 'ContactsAcceptContact', None))
ContactsAcceptContact = getattr(_fn, 'ContactsAcceptContact', None)
GetLocated = getattr(_fn, 'GetLocated', getattr(_fn, 'ContactsGetLocated', None))
ContactsGetLocated = getattr(_fn, 'ContactsGetLocated', None)
BlockFromReplies = getattr(_fn, 'BlockFromReplies', getattr(_fn, 'ContactsBlockFromReplies', None))
ContactsBlockFromReplies = getattr(_fn, 'ContactsBlockFromReplies', None)
ResolvePhone = getattr(_fn, 'ResolvePhone', getattr(_fn, 'ContactsResolvePhone', None))
ContactsResolvePhone = getattr(_fn, 'ContactsResolvePhone', None)
ExportContactToken = getattr(_fn, 'ExportContactToken', getattr(_fn, 'ContactsExportContactToken', None))
ContactsExportContactToken = getattr(_fn, 'ContactsExportContactToken', None)
ImportContactToken = getattr(_fn, 'ImportContactToken', getattr(_fn, 'ContactsImportContactToken', None))
ContactsImportContactToken = getattr(_fn, 'ContactsImportContactToken', None)
EditCloseFriends = getattr(_fn, 'EditCloseFriends', getattr(_fn, 'ContactsEditCloseFriends', None))
ContactsEditCloseFriends = getattr(_fn, 'ContactsEditCloseFriends', None)
SetBlocked = getattr(_fn, 'SetBlocked', getattr(_fn, 'ContactsSetBlocked', None))
ContactsSetBlocked = getattr(_fn, 'ContactsSetBlocked', None)
GetBirthdays = getattr(_fn, 'GetBirthdays', getattr(_fn, 'ContactsGetBirthdays', None))
ContactsGetBirthdays = getattr(_fn, 'ContactsGetBirthdays', None)
GetSponsoredPeers = getattr(_fn, 'GetSponsoredPeers', getattr(_fn, 'ContactsGetSponsoredPeers', None))
ContactsGetSponsoredPeers = getattr(_fn, 'ContactsGetSponsoredPeers', None)
UpdateContactNote = getattr(_fn, 'UpdateContactNote', getattr(_fn, 'ContactsUpdateContactNote', None))
ContactsUpdateContactNote = getattr(_fn, 'ContactsUpdateContactNote', None)

__all__ = [
    "GetContactIDs",
    "ContactsGetContactIDs",
    "GetStatuses",
    "ContactsGetStatuses",
    "GetContacts",
    "ContactsGetContacts",
    "ImportContacts",
    "ContactsImportContacts",
    "DeleteContacts",
    "ContactsDeleteContacts",
    "DeleteByPhones",
    "ContactsDeleteByPhones",
    "Block",
    "ContactsBlock",
    "Unblock",
    "ContactsUnblock",
    "GetBlocked",
    "ContactsGetBlocked",
    "Search",
    "ContactsSearch",
    "ResolveUsername",
    "ContactsResolveUsername",
    "GetTopPeers",
    "ContactsGetTopPeers",
    "ResetTopPeerRating",
    "ContactsResetTopPeerRating",
    "ResetSaved",
    "ContactsResetSaved",
    "GetSaved",
    "ContactsGetSaved",
    "ToggleTopPeers",
    "ContactsToggleTopPeers",
    "AddContact",
    "ContactsAddContact",
    "AcceptContact",
    "ContactsAcceptContact",
    "GetLocated",
    "ContactsGetLocated",
    "BlockFromReplies",
    "ContactsBlockFromReplies",
    "ResolvePhone",
    "ContactsResolvePhone",
    "ExportContactToken",
    "ContactsExportContactToken",
    "ImportContactToken",
    "ContactsImportContactToken",
    "EditCloseFriends",
    "ContactsEditCloseFriends",
    "SetBlocked",
    "ContactsSetBlocked",
    "GetBirthdays",
    "ContactsGetBirthdays",
    "GetSponsoredPeers",
    "ContactsGetSponsoredPeers",
    "UpdateContactNote",
    "ContactsUpdateContactNote"
]
