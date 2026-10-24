from ...tl import functions as _fn


ExportChatlistInvite = getattr(_fn, 'ExportChatlistInvite', getattr(_fn, 'ChatlistsExportChatlistInvite', None))
ChatlistsExportChatlistInvite = getattr(_fn, 'ChatlistsExportChatlistInvite', None)
DeleteExportedInvite = getattr(_fn, 'DeleteExportedInvite', getattr(_fn, 'ChatlistsDeleteExportedInvite', None))
ChatlistsDeleteExportedInvite = getattr(_fn, 'ChatlistsDeleteExportedInvite', None)
EditExportedInvite = getattr(_fn, 'EditExportedInvite', getattr(_fn, 'ChatlistsEditExportedInvite', None))
ChatlistsEditExportedInvite = getattr(_fn, 'ChatlistsEditExportedInvite', None)
GetExportedInvites = getattr(_fn, 'GetExportedInvites', getattr(_fn, 'ChatlistsGetExportedInvites', None))
ChatlistsGetExportedInvites = getattr(_fn, 'ChatlistsGetExportedInvites', None)
CheckChatlistInvite = getattr(_fn, 'CheckChatlistInvite', getattr(_fn, 'ChatlistsCheckChatlistInvite', None))
ChatlistsCheckChatlistInvite = getattr(_fn, 'ChatlistsCheckChatlistInvite', None)
JoinChatlistInvite = getattr(_fn, 'JoinChatlistInvite', getattr(_fn, 'ChatlistsJoinChatlistInvite', None))
ChatlistsJoinChatlistInvite = getattr(_fn, 'ChatlistsJoinChatlistInvite', None)
GetChatlistUpdates = getattr(_fn, 'GetChatlistUpdates', getattr(_fn, 'ChatlistsGetChatlistUpdates', None))
ChatlistsGetChatlistUpdates = getattr(_fn, 'ChatlistsGetChatlistUpdates', None)
JoinChatlistUpdates = getattr(_fn, 'JoinChatlistUpdates', getattr(_fn, 'ChatlistsJoinChatlistUpdates', None))
ChatlistsJoinChatlistUpdates = getattr(_fn, 'ChatlistsJoinChatlistUpdates', None)
HideChatlistUpdates = getattr(_fn, 'HideChatlistUpdates', getattr(_fn, 'ChatlistsHideChatlistUpdates', None))
ChatlistsHideChatlistUpdates = getattr(_fn, 'ChatlistsHideChatlistUpdates', None)
GetLeaveChatlistSuggestions = getattr(_fn, 'GetLeaveChatlistSuggestions', getattr(_fn, 'ChatlistsGetLeaveChatlistSuggestions', None))
ChatlistsGetLeaveChatlistSuggestions = getattr(_fn, 'ChatlistsGetLeaveChatlistSuggestions', None)
LeaveChatlist = getattr(_fn, 'LeaveChatlist', getattr(_fn, 'ChatlistsLeaveChatlist', None))
ChatlistsLeaveChatlist = getattr(_fn, 'ChatlistsLeaveChatlist', None)

__all__ = [
    "ExportChatlistInvite",
    "ChatlistsExportChatlistInvite",
    "DeleteExportedInvite",
    "ChatlistsDeleteExportedInvite",
    "EditExportedInvite",
    "ChatlistsEditExportedInvite",
    "GetExportedInvites",
    "ChatlistsGetExportedInvites",
    "CheckChatlistInvite",
    "ChatlistsCheckChatlistInvite",
    "JoinChatlistInvite",
    "ChatlistsJoinChatlistInvite",
    "GetChatlistUpdates",
    "ChatlistsGetChatlistUpdates",
    "JoinChatlistUpdates",
    "ChatlistsJoinChatlistUpdates",
    "HideChatlistUpdates",
    "ChatlistsHideChatlistUpdates",
    "GetLeaveChatlistSuggestions",
    "ChatlistsGetLeaveChatlistSuggestions",
    "LeaveChatlist",
    "ChatlistsLeaveChatlist"
]
