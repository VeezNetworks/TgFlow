from ...tl import functions as _fn


GetMessages = getattr(_fn, 'GetMessages', getattr(_fn, 'MessagesGetMessages', None))
MessagesGetMessages = getattr(_fn, 'MessagesGetMessages', None)
GetDialogs = getattr(_fn, 'GetDialogs', getattr(_fn, 'MessagesGetDialogs', None))
MessagesGetDialogs = getattr(_fn, 'MessagesGetDialogs', None)
GetHistory = getattr(_fn, 'GetHistory', getattr(_fn, 'MessagesGetHistory', None))
MessagesGetHistory = getattr(_fn, 'MessagesGetHistory', None)
Search = getattr(_fn, 'Search', getattr(_fn, 'MessagesSearch', None))
MessagesSearch = getattr(_fn, 'MessagesSearch', None)
ReadHistory = getattr(_fn, 'ReadHistory', getattr(_fn, 'MessagesReadHistory', None))
MessagesReadHistory = getattr(_fn, 'MessagesReadHistory', None)
DeleteHistory = getattr(_fn, 'DeleteHistory', getattr(_fn, 'MessagesDeleteHistory', None))
MessagesDeleteHistory = getattr(_fn, 'MessagesDeleteHistory', None)
DeleteMessages = getattr(_fn, 'DeleteMessages', getattr(_fn, 'MessagesDeleteMessages', None))
MessagesDeleteMessages = getattr(_fn, 'MessagesDeleteMessages', None)
ReceivedMessages = getattr(_fn, 'ReceivedMessages', getattr(_fn, 'MessagesReceivedMessages', None))
MessagesReceivedMessages = getattr(_fn, 'MessagesReceivedMessages', None)
SetTyping = getattr(_fn, 'SetTyping', getattr(_fn, 'MessagesSetTyping', None))
MessagesSetTyping = getattr(_fn, 'MessagesSetTyping', None)
SendMessage = getattr(_fn, 'SendMessage', getattr(_fn, 'MessagesSendMessage', None))
MessagesSendMessage = getattr(_fn, 'MessagesSendMessage', None)
SendMedia = getattr(_fn, 'SendMedia', getattr(_fn, 'MessagesSendMedia', None))
MessagesSendMedia = getattr(_fn, 'MessagesSendMedia', None)
ForwardMessages = getattr(_fn, 'ForwardMessages', getattr(_fn, 'MessagesForwardMessages', None))
MessagesForwardMessages = getattr(_fn, 'MessagesForwardMessages', None)
ReportSpam = getattr(_fn, 'ReportSpam', getattr(_fn, 'MessagesReportSpam', None))
MessagesReportSpam = getattr(_fn, 'MessagesReportSpam', None)
GetPeerSettings = getattr(_fn, 'GetPeerSettings', getattr(_fn, 'MessagesGetPeerSettings', None))
MessagesGetPeerSettings = getattr(_fn, 'MessagesGetPeerSettings', None)
Report = getattr(_fn, 'Report', getattr(_fn, 'MessagesReport', None))
MessagesReport = getattr(_fn, 'MessagesReport', None)
GetChats = getattr(_fn, 'GetChats', getattr(_fn, 'MessagesGetChats', None))
MessagesGetChats = getattr(_fn, 'MessagesGetChats', None)
GetFullChat = getattr(_fn, 'GetFullChat', getattr(_fn, 'MessagesGetFullChat', None))
MessagesGetFullChat = getattr(_fn, 'MessagesGetFullChat', None)
EditChatTitle = getattr(_fn, 'EditChatTitle', getattr(_fn, 'MessagesEditChatTitle', None))
MessagesEditChatTitle = getattr(_fn, 'MessagesEditChatTitle', None)
EditChatPhoto = getattr(_fn, 'EditChatPhoto', getattr(_fn, 'MessagesEditChatPhoto', None))
MessagesEditChatPhoto = getattr(_fn, 'MessagesEditChatPhoto', None)
AddChatUser = getattr(_fn, 'AddChatUser', getattr(_fn, 'MessagesAddChatUser', None))
MessagesAddChatUser = getattr(_fn, 'MessagesAddChatUser', None)
DeleteChatUser = getattr(_fn, 'DeleteChatUser', getattr(_fn, 'MessagesDeleteChatUser', None))
MessagesDeleteChatUser = getattr(_fn, 'MessagesDeleteChatUser', None)
CreateChat = getattr(_fn, 'CreateChat', getattr(_fn, 'MessagesCreateChat', None))
MessagesCreateChat = getattr(_fn, 'MessagesCreateChat', None)
GetDhConfig = getattr(_fn, 'GetDhConfig', getattr(_fn, 'MessagesGetDhConfig', None))
MessagesGetDhConfig = getattr(_fn, 'MessagesGetDhConfig', None)
RequestEncryption = getattr(_fn, 'RequestEncryption', getattr(_fn, 'MessagesRequestEncryption', None))
MessagesRequestEncryption = getattr(_fn, 'MessagesRequestEncryption', None)
AcceptEncryption = getattr(_fn, 'AcceptEncryption', getattr(_fn, 'MessagesAcceptEncryption', None))
MessagesAcceptEncryption = getattr(_fn, 'MessagesAcceptEncryption', None)
DiscardEncryption = getattr(_fn, 'DiscardEncryption', getattr(_fn, 'MessagesDiscardEncryption', None))
MessagesDiscardEncryption = getattr(_fn, 'MessagesDiscardEncryption', None)
SetEncryptedTyping = getattr(_fn, 'SetEncryptedTyping', getattr(_fn, 'MessagesSetEncryptedTyping', None))
MessagesSetEncryptedTyping = getattr(_fn, 'MessagesSetEncryptedTyping', None)
ReadEncryptedHistory = getattr(_fn, 'ReadEncryptedHistory', getattr(_fn, 'MessagesReadEncryptedHistory', None))
MessagesReadEncryptedHistory = getattr(_fn, 'MessagesReadEncryptedHistory', None)
SendEncrypted = getattr(_fn, 'SendEncrypted', getattr(_fn, 'MessagesSendEncrypted', None))
MessagesSendEncrypted = getattr(_fn, 'MessagesSendEncrypted', None)
SendEncryptedFile = getattr(_fn, 'SendEncryptedFile', getattr(_fn, 'MessagesSendEncryptedFile', None))
MessagesSendEncryptedFile = getattr(_fn, 'MessagesSendEncryptedFile', None)
SendEncryptedService = getattr(_fn, 'SendEncryptedService', getattr(_fn, 'MessagesSendEncryptedService', None))
MessagesSendEncryptedService = getattr(_fn, 'MessagesSendEncryptedService', None)
ReceivedQueue = getattr(_fn, 'ReceivedQueue', getattr(_fn, 'MessagesReceivedQueue', None))
MessagesReceivedQueue = getattr(_fn, 'MessagesReceivedQueue', None)
ReportEncryptedSpam = getattr(_fn, 'ReportEncryptedSpam', getattr(_fn, 'MessagesReportEncryptedSpam', None))
MessagesReportEncryptedSpam = getattr(_fn, 'MessagesReportEncryptedSpam', None)
ReadMessageContents = getattr(_fn, 'ReadMessageContents', getattr(_fn, 'MessagesReadMessageContents', None))
MessagesReadMessageContents = getattr(_fn, 'MessagesReadMessageContents', None)
GetStickers = getattr(_fn, 'GetStickers', getattr(_fn, 'MessagesGetStickers', None))
MessagesGetStickers = getattr(_fn, 'MessagesGetStickers', None)
GetAllStickers = getattr(_fn, 'GetAllStickers', getattr(_fn, 'MessagesGetAllStickers', None))
MessagesGetAllStickers = getattr(_fn, 'MessagesGetAllStickers', None)
GetWebPagePreview = getattr(_fn, 'GetWebPagePreview', getattr(_fn, 'MessagesGetWebPagePreview', None))
MessagesGetWebPagePreview = getattr(_fn, 'MessagesGetWebPagePreview', None)
ExportChatInvite = getattr(_fn, 'ExportChatInvite', getattr(_fn, 'MessagesExportChatInvite', None))
MessagesExportChatInvite = getattr(_fn, 'MessagesExportChatInvite', None)
CheckChatInvite = getattr(_fn, 'CheckChatInvite', getattr(_fn, 'MessagesCheckChatInvite', None))
MessagesCheckChatInvite = getattr(_fn, 'MessagesCheckChatInvite', None)
ImportChatInvite = getattr(_fn, 'ImportChatInvite', getattr(_fn, 'MessagesImportChatInvite', None))
MessagesImportChatInvite = getattr(_fn, 'MessagesImportChatInvite', None)
GetStickerSet = getattr(_fn, 'GetStickerSet', getattr(_fn, 'MessagesGetStickerSet', None))
MessagesGetStickerSet = getattr(_fn, 'MessagesGetStickerSet', None)
InstallStickerSet = getattr(_fn, 'InstallStickerSet', getattr(_fn, 'MessagesInstallStickerSet', None))
MessagesInstallStickerSet = getattr(_fn, 'MessagesInstallStickerSet', None)
UninstallStickerSet = getattr(_fn, 'UninstallStickerSet', getattr(_fn, 'MessagesUninstallStickerSet', None))
MessagesUninstallStickerSet = getattr(_fn, 'MessagesUninstallStickerSet', None)
StartBot = getattr(_fn, 'StartBot', getattr(_fn, 'MessagesStartBot', None))
MessagesStartBot = getattr(_fn, 'MessagesStartBot', None)
GetMessagesViews = getattr(_fn, 'GetMessagesViews', getattr(_fn, 'MessagesGetMessagesViews', None))
MessagesGetMessagesViews = getattr(_fn, 'MessagesGetMessagesViews', None)
EditChatAdmin = getattr(_fn, 'EditChatAdmin', getattr(_fn, 'MessagesEditChatAdmin', None))
MessagesEditChatAdmin = getattr(_fn, 'MessagesEditChatAdmin', None)
MigrateChat = getattr(_fn, 'MigrateChat', getattr(_fn, 'MessagesMigrateChat', None))
MessagesMigrateChat = getattr(_fn, 'MessagesMigrateChat', None)
SearchGlobal = getattr(_fn, 'SearchGlobal', getattr(_fn, 'MessagesSearchGlobal', None))
MessagesSearchGlobal = getattr(_fn, 'MessagesSearchGlobal', None)
ReorderStickerSets = getattr(_fn, 'ReorderStickerSets', getattr(_fn, 'MessagesReorderStickerSets', None))
MessagesReorderStickerSets = getattr(_fn, 'MessagesReorderStickerSets', None)
GetDocumentByHash = getattr(_fn, 'GetDocumentByHash', getattr(_fn, 'MessagesGetDocumentByHash', None))
MessagesGetDocumentByHash = getattr(_fn, 'MessagesGetDocumentByHash', None)
GetSavedGifs = getattr(_fn, 'GetSavedGifs', getattr(_fn, 'MessagesGetSavedGifs', None))
MessagesGetSavedGifs = getattr(_fn, 'MessagesGetSavedGifs', None)
SaveGif = getattr(_fn, 'SaveGif', getattr(_fn, 'MessagesSaveGif', None))
MessagesSaveGif = getattr(_fn, 'MessagesSaveGif', None)
GetInlineBotResults = getattr(_fn, 'GetInlineBotResults', getattr(_fn, 'MessagesGetInlineBotResults', None))
MessagesGetInlineBotResults = getattr(_fn, 'MessagesGetInlineBotResults', None)
SetInlineBotResults = getattr(_fn, 'SetInlineBotResults', getattr(_fn, 'MessagesSetInlineBotResults', None))
MessagesSetInlineBotResults = getattr(_fn, 'MessagesSetInlineBotResults', None)
SendInlineBotResult = getattr(_fn, 'SendInlineBotResult', getattr(_fn, 'MessagesSendInlineBotResult', None))
MessagesSendInlineBotResult = getattr(_fn, 'MessagesSendInlineBotResult', None)
GetMessageEditData = getattr(_fn, 'GetMessageEditData', getattr(_fn, 'MessagesGetMessageEditData', None))
MessagesGetMessageEditData = getattr(_fn, 'MessagesGetMessageEditData', None)
EditMessage = getattr(_fn, 'EditMessage', getattr(_fn, 'MessagesEditMessage', None))
MessagesEditMessage = getattr(_fn, 'MessagesEditMessage', None)
EditInlineBotMessage = getattr(_fn, 'EditInlineBotMessage', getattr(_fn, 'MessagesEditInlineBotMessage', None))
MessagesEditInlineBotMessage = getattr(_fn, 'MessagesEditInlineBotMessage', None)
GetBotCallbackAnswer = getattr(_fn, 'GetBotCallbackAnswer', getattr(_fn, 'MessagesGetBotCallbackAnswer', None))
MessagesGetBotCallbackAnswer = getattr(_fn, 'MessagesGetBotCallbackAnswer', None)
SetBotCallbackAnswer = getattr(_fn, 'SetBotCallbackAnswer', getattr(_fn, 'MessagesSetBotCallbackAnswer', None))
MessagesSetBotCallbackAnswer = getattr(_fn, 'MessagesSetBotCallbackAnswer', None)
GetPeerDialogs = getattr(_fn, 'GetPeerDialogs', getattr(_fn, 'MessagesGetPeerDialogs', None))
MessagesGetPeerDialogs = getattr(_fn, 'MessagesGetPeerDialogs', None)
SaveDraft = getattr(_fn, 'SaveDraft', getattr(_fn, 'MessagesSaveDraft', None))
MessagesSaveDraft = getattr(_fn, 'MessagesSaveDraft', None)
GetAllDrafts = getattr(_fn, 'GetAllDrafts', getattr(_fn, 'MessagesGetAllDrafts', None))
MessagesGetAllDrafts = getattr(_fn, 'MessagesGetAllDrafts', None)
GetFeaturedStickers = getattr(_fn, 'GetFeaturedStickers', getattr(_fn, 'MessagesGetFeaturedStickers', None))
MessagesGetFeaturedStickers = getattr(_fn, 'MessagesGetFeaturedStickers', None)
ReadFeaturedStickers = getattr(_fn, 'ReadFeaturedStickers', getattr(_fn, 'MessagesReadFeaturedStickers', None))
MessagesReadFeaturedStickers = getattr(_fn, 'MessagesReadFeaturedStickers', None)
GetRecentStickers = getattr(_fn, 'GetRecentStickers', getattr(_fn, 'MessagesGetRecentStickers', None))
MessagesGetRecentStickers = getattr(_fn, 'MessagesGetRecentStickers', None)
SaveRecentSticker = getattr(_fn, 'SaveRecentSticker', getattr(_fn, 'MessagesSaveRecentSticker', None))
MessagesSaveRecentSticker = getattr(_fn, 'MessagesSaveRecentSticker', None)
ClearRecentStickers = getattr(_fn, 'ClearRecentStickers', getattr(_fn, 'MessagesClearRecentStickers', None))
MessagesClearRecentStickers = getattr(_fn, 'MessagesClearRecentStickers', None)
GetArchivedStickers = getattr(_fn, 'GetArchivedStickers', getattr(_fn, 'MessagesGetArchivedStickers', None))
MessagesGetArchivedStickers = getattr(_fn, 'MessagesGetArchivedStickers', None)
GetMaskStickers = getattr(_fn, 'GetMaskStickers', getattr(_fn, 'MessagesGetMaskStickers', None))
MessagesGetMaskStickers = getattr(_fn, 'MessagesGetMaskStickers', None)
GetAttachedStickers = getattr(_fn, 'GetAttachedStickers', getattr(_fn, 'MessagesGetAttachedStickers', None))
MessagesGetAttachedStickers = getattr(_fn, 'MessagesGetAttachedStickers', None)
SetGameScore = getattr(_fn, 'SetGameScore', getattr(_fn, 'MessagesSetGameScore', None))
MessagesSetGameScore = getattr(_fn, 'MessagesSetGameScore', None)
SetInlineGameScore = getattr(_fn, 'SetInlineGameScore', getattr(_fn, 'MessagesSetInlineGameScore', None))
MessagesSetInlineGameScore = getattr(_fn, 'MessagesSetInlineGameScore', None)
GetGameHighScores = getattr(_fn, 'GetGameHighScores', getattr(_fn, 'MessagesGetGameHighScores', None))
MessagesGetGameHighScores = getattr(_fn, 'MessagesGetGameHighScores', None)
GetInlineGameHighScores = getattr(_fn, 'GetInlineGameHighScores', getattr(_fn, 'MessagesGetInlineGameHighScores', None))
MessagesGetInlineGameHighScores = getattr(_fn, 'MessagesGetInlineGameHighScores', None)
GetCommonChats = getattr(_fn, 'GetCommonChats', getattr(_fn, 'MessagesGetCommonChats', None))
MessagesGetCommonChats = getattr(_fn, 'MessagesGetCommonChats', None)
GetWebPage = getattr(_fn, 'GetWebPage', getattr(_fn, 'MessagesGetWebPage', None))
MessagesGetWebPage = getattr(_fn, 'MessagesGetWebPage', None)
ToggleDialogPin = getattr(_fn, 'ToggleDialogPin', getattr(_fn, 'MessagesToggleDialogPin', None))
MessagesToggleDialogPin = getattr(_fn, 'MessagesToggleDialogPin', None)
ReorderPinnedDialogs = getattr(_fn, 'ReorderPinnedDialogs', getattr(_fn, 'MessagesReorderPinnedDialogs', None))
MessagesReorderPinnedDialogs = getattr(_fn, 'MessagesReorderPinnedDialogs', None)
GetPinnedDialogs = getattr(_fn, 'GetPinnedDialogs', getattr(_fn, 'MessagesGetPinnedDialogs', None))
MessagesGetPinnedDialogs = getattr(_fn, 'MessagesGetPinnedDialogs', None)
SetBotShippingResults = getattr(_fn, 'SetBotShippingResults', getattr(_fn, 'MessagesSetBotShippingResults', None))
MessagesSetBotShippingResults = getattr(_fn, 'MessagesSetBotShippingResults', None)
SetBotPrecheckoutResults = getattr(_fn, 'SetBotPrecheckoutResults', getattr(_fn, 'MessagesSetBotPrecheckoutResults', None))
MessagesSetBotPrecheckoutResults = getattr(_fn, 'MessagesSetBotPrecheckoutResults', None)
UploadMedia = getattr(_fn, 'UploadMedia', getattr(_fn, 'MessagesUploadMedia', None))
MessagesUploadMedia = getattr(_fn, 'MessagesUploadMedia', None)
SendScreenshotNotification = getattr(_fn, 'SendScreenshotNotification', getattr(_fn, 'MessagesSendScreenshotNotification', None))
MessagesSendScreenshotNotification = getattr(_fn, 'MessagesSendScreenshotNotification', None)
GetFavedStickers = getattr(_fn, 'GetFavedStickers', getattr(_fn, 'MessagesGetFavedStickers', None))
MessagesGetFavedStickers = getattr(_fn, 'MessagesGetFavedStickers', None)
FaveSticker = getattr(_fn, 'FaveSticker', getattr(_fn, 'MessagesFaveSticker', None))
MessagesFaveSticker = getattr(_fn, 'MessagesFaveSticker', None)
GetUnreadMentions = getattr(_fn, 'GetUnreadMentions', getattr(_fn, 'MessagesGetUnreadMentions', None))
MessagesGetUnreadMentions = getattr(_fn, 'MessagesGetUnreadMentions', None)
ReadMentions = getattr(_fn, 'ReadMentions', getattr(_fn, 'MessagesReadMentions', None))
MessagesReadMentions = getattr(_fn, 'MessagesReadMentions', None)
GetRecentLocations = getattr(_fn, 'GetRecentLocations', getattr(_fn, 'MessagesGetRecentLocations', None))
MessagesGetRecentLocations = getattr(_fn, 'MessagesGetRecentLocations', None)
SendMultiMedia = getattr(_fn, 'SendMultiMedia', getattr(_fn, 'MessagesSendMultiMedia', None))
MessagesSendMultiMedia = getattr(_fn, 'MessagesSendMultiMedia', None)
UploadEncryptedFile = getattr(_fn, 'UploadEncryptedFile', getattr(_fn, 'MessagesUploadEncryptedFile', None))
MessagesUploadEncryptedFile = getattr(_fn, 'MessagesUploadEncryptedFile', None)
SearchStickerSets = getattr(_fn, 'SearchStickerSets', getattr(_fn, 'MessagesSearchStickerSets', None))
MessagesSearchStickerSets = getattr(_fn, 'MessagesSearchStickerSets', None)
GetSplitRanges = getattr(_fn, 'GetSplitRanges', getattr(_fn, 'MessagesGetSplitRanges', None))
MessagesGetSplitRanges = getattr(_fn, 'MessagesGetSplitRanges', None)
MarkDialogUnread = getattr(_fn, 'MarkDialogUnread', getattr(_fn, 'MessagesMarkDialogUnread', None))
MessagesMarkDialogUnread = getattr(_fn, 'MessagesMarkDialogUnread', None)
GetDialogUnreadMarks = getattr(_fn, 'GetDialogUnreadMarks', getattr(_fn, 'MessagesGetDialogUnreadMarks', None))
MessagesGetDialogUnreadMarks = getattr(_fn, 'MessagesGetDialogUnreadMarks', None)
ClearAllDrafts = getattr(_fn, 'ClearAllDrafts', getattr(_fn, 'MessagesClearAllDrafts', None))
MessagesClearAllDrafts = getattr(_fn, 'MessagesClearAllDrafts', None)
UpdatePinnedMessage = getattr(_fn, 'UpdatePinnedMessage', getattr(_fn, 'MessagesUpdatePinnedMessage', None))
MessagesUpdatePinnedMessage = getattr(_fn, 'MessagesUpdatePinnedMessage', None)
SendVote = getattr(_fn, 'SendVote', getattr(_fn, 'MessagesSendVote', None))
MessagesSendVote = getattr(_fn, 'MessagesSendVote', None)
GetPollResults = getattr(_fn, 'GetPollResults', getattr(_fn, 'MessagesGetPollResults', None))
MessagesGetPollResults = getattr(_fn, 'MessagesGetPollResults', None)
GetOnlines = getattr(_fn, 'GetOnlines', getattr(_fn, 'MessagesGetOnlines', None))
MessagesGetOnlines = getattr(_fn, 'MessagesGetOnlines', None)
EditChatAbout = getattr(_fn, 'EditChatAbout', getattr(_fn, 'MessagesEditChatAbout', None))
MessagesEditChatAbout = getattr(_fn, 'MessagesEditChatAbout', None)
EditChatDefaultBannedRights = getattr(_fn, 'EditChatDefaultBannedRights', getattr(_fn, 'MessagesEditChatDefaultBannedRights', None))
MessagesEditChatDefaultBannedRights = getattr(_fn, 'MessagesEditChatDefaultBannedRights', None)
GetEmojiKeywords = getattr(_fn, 'GetEmojiKeywords', getattr(_fn, 'MessagesGetEmojiKeywords', None))
MessagesGetEmojiKeywords = getattr(_fn, 'MessagesGetEmojiKeywords', None)
GetEmojiKeywordsDifference = getattr(_fn, 'GetEmojiKeywordsDifference', getattr(_fn, 'MessagesGetEmojiKeywordsDifference', None))
MessagesGetEmojiKeywordsDifference = getattr(_fn, 'MessagesGetEmojiKeywordsDifference', None)
GetEmojiKeywordsLanguages = getattr(_fn, 'GetEmojiKeywordsLanguages', getattr(_fn, 'MessagesGetEmojiKeywordsLanguages', None))
MessagesGetEmojiKeywordsLanguages = getattr(_fn, 'MessagesGetEmojiKeywordsLanguages', None)
GetEmojiURL = getattr(_fn, 'GetEmojiURL', getattr(_fn, 'MessagesGetEmojiURL', None))
MessagesGetEmojiURL = getattr(_fn, 'MessagesGetEmojiURL', None)
GetSearchCounters = getattr(_fn, 'GetSearchCounters', getattr(_fn, 'MessagesGetSearchCounters', None))
MessagesGetSearchCounters = getattr(_fn, 'MessagesGetSearchCounters', None)
RequestUrlAuth = getattr(_fn, 'RequestUrlAuth', getattr(_fn, 'MessagesRequestUrlAuth', None))
MessagesRequestUrlAuth = getattr(_fn, 'MessagesRequestUrlAuth', None)
AcceptUrlAuth = getattr(_fn, 'AcceptUrlAuth', getattr(_fn, 'MessagesAcceptUrlAuth', None))
MessagesAcceptUrlAuth = getattr(_fn, 'MessagesAcceptUrlAuth', None)
HidePeerSettingsBar = getattr(_fn, 'HidePeerSettingsBar', getattr(_fn, 'MessagesHidePeerSettingsBar', None))
MessagesHidePeerSettingsBar = getattr(_fn, 'MessagesHidePeerSettingsBar', None)
GetScheduledHistory = getattr(_fn, 'GetScheduledHistory', getattr(_fn, 'MessagesGetScheduledHistory', None))
MessagesGetScheduledHistory = getattr(_fn, 'MessagesGetScheduledHistory', None)
GetScheduledMessages = getattr(_fn, 'GetScheduledMessages', getattr(_fn, 'MessagesGetScheduledMessages', None))
MessagesGetScheduledMessages = getattr(_fn, 'MessagesGetScheduledMessages', None)
SendScheduledMessages = getattr(_fn, 'SendScheduledMessages', getattr(_fn, 'MessagesSendScheduledMessages', None))
MessagesSendScheduledMessages = getattr(_fn, 'MessagesSendScheduledMessages', None)
DeleteScheduledMessages = getattr(_fn, 'DeleteScheduledMessages', getattr(_fn, 'MessagesDeleteScheduledMessages', None))
MessagesDeleteScheduledMessages = getattr(_fn, 'MessagesDeleteScheduledMessages', None)
GetPollVotes = getattr(_fn, 'GetPollVotes', getattr(_fn, 'MessagesGetPollVotes', None))
MessagesGetPollVotes = getattr(_fn, 'MessagesGetPollVotes', None)
ToggleStickerSets = getattr(_fn, 'ToggleStickerSets', getattr(_fn, 'MessagesToggleStickerSets', None))
MessagesToggleStickerSets = getattr(_fn, 'MessagesToggleStickerSets', None)
GetDialogFilters = getattr(_fn, 'GetDialogFilters', getattr(_fn, 'MessagesGetDialogFilters', None))
MessagesGetDialogFilters = getattr(_fn, 'MessagesGetDialogFilters', None)
GetSuggestedDialogFilters = getattr(_fn, 'GetSuggestedDialogFilters', getattr(_fn, 'MessagesGetSuggestedDialogFilters', None))
MessagesGetSuggestedDialogFilters = getattr(_fn, 'MessagesGetSuggestedDialogFilters', None)
UpdateDialogFilter = getattr(_fn, 'UpdateDialogFilter', getattr(_fn, 'MessagesUpdateDialogFilter', None))
MessagesUpdateDialogFilter = getattr(_fn, 'MessagesUpdateDialogFilter', None)
UpdateDialogFiltersOrder = getattr(_fn, 'UpdateDialogFiltersOrder', getattr(_fn, 'MessagesUpdateDialogFiltersOrder', None))
MessagesUpdateDialogFiltersOrder = getattr(_fn, 'MessagesUpdateDialogFiltersOrder', None)
GetOldFeaturedStickers = getattr(_fn, 'GetOldFeaturedStickers', getattr(_fn, 'MessagesGetOldFeaturedStickers', None))
MessagesGetOldFeaturedStickers = getattr(_fn, 'MessagesGetOldFeaturedStickers', None)
GetReplies = getattr(_fn, 'GetReplies', getattr(_fn, 'MessagesGetReplies', None))
MessagesGetReplies = getattr(_fn, 'MessagesGetReplies', None)
GetDiscussionMessage = getattr(_fn, 'GetDiscussionMessage', getattr(_fn, 'MessagesGetDiscussionMessage', None))
MessagesGetDiscussionMessage = getattr(_fn, 'MessagesGetDiscussionMessage', None)
ReadDiscussion = getattr(_fn, 'ReadDiscussion', getattr(_fn, 'MessagesReadDiscussion', None))
MessagesReadDiscussion = getattr(_fn, 'MessagesReadDiscussion', None)
UnpinAllMessages = getattr(_fn, 'UnpinAllMessages', getattr(_fn, 'MessagesUnpinAllMessages', None))
MessagesUnpinAllMessages = getattr(_fn, 'MessagesUnpinAllMessages', None)
DeleteChat = getattr(_fn, 'DeleteChat', getattr(_fn, 'MessagesDeleteChat', None))
MessagesDeleteChat = getattr(_fn, 'MessagesDeleteChat', None)
DeletePhoneCallHistory = getattr(_fn, 'DeletePhoneCallHistory', getattr(_fn, 'MessagesDeletePhoneCallHistory', None))
MessagesDeletePhoneCallHistory = getattr(_fn, 'MessagesDeletePhoneCallHistory', None)
CheckHistoryImport = getattr(_fn, 'CheckHistoryImport', getattr(_fn, 'MessagesCheckHistoryImport', None))
MessagesCheckHistoryImport = getattr(_fn, 'MessagesCheckHistoryImport', None)
InitHistoryImport = getattr(_fn, 'InitHistoryImport', getattr(_fn, 'MessagesInitHistoryImport', None))
MessagesInitHistoryImport = getattr(_fn, 'MessagesInitHistoryImport', None)
UploadImportedMedia = getattr(_fn, 'UploadImportedMedia', getattr(_fn, 'MessagesUploadImportedMedia', None))
MessagesUploadImportedMedia = getattr(_fn, 'MessagesUploadImportedMedia', None)
StartHistoryImport = getattr(_fn, 'StartHistoryImport', getattr(_fn, 'MessagesStartHistoryImport', None))
MessagesStartHistoryImport = getattr(_fn, 'MessagesStartHistoryImport', None)
GetExportedChatInvites = getattr(_fn, 'GetExportedChatInvites', getattr(_fn, 'MessagesGetExportedChatInvites', None))
MessagesGetExportedChatInvites = getattr(_fn, 'MessagesGetExportedChatInvites', None)
GetExportedChatInvite = getattr(_fn, 'GetExportedChatInvite', getattr(_fn, 'MessagesGetExportedChatInvite', None))
MessagesGetExportedChatInvite = getattr(_fn, 'MessagesGetExportedChatInvite', None)
EditExportedChatInvite = getattr(_fn, 'EditExportedChatInvite', getattr(_fn, 'MessagesEditExportedChatInvite', None))
MessagesEditExportedChatInvite = getattr(_fn, 'MessagesEditExportedChatInvite', None)
DeleteRevokedExportedChatInvites = getattr(_fn, 'DeleteRevokedExportedChatInvites', getattr(_fn, 'MessagesDeleteRevokedExportedChatInvites', None))
MessagesDeleteRevokedExportedChatInvites = getattr(_fn, 'MessagesDeleteRevokedExportedChatInvites', None)
DeleteExportedChatInvite = getattr(_fn, 'DeleteExportedChatInvite', getattr(_fn, 'MessagesDeleteExportedChatInvite', None))
MessagesDeleteExportedChatInvite = getattr(_fn, 'MessagesDeleteExportedChatInvite', None)
GetAdminsWithInvites = getattr(_fn, 'GetAdminsWithInvites', getattr(_fn, 'MessagesGetAdminsWithInvites', None))
MessagesGetAdminsWithInvites = getattr(_fn, 'MessagesGetAdminsWithInvites', None)
GetChatInviteImporters = getattr(_fn, 'GetChatInviteImporters', getattr(_fn, 'MessagesGetChatInviteImporters', None))
MessagesGetChatInviteImporters = getattr(_fn, 'MessagesGetChatInviteImporters', None)
SetHistoryTTL = getattr(_fn, 'SetHistoryTTL', getattr(_fn, 'MessagesSetHistoryTTL', None))
MessagesSetHistoryTTL = getattr(_fn, 'MessagesSetHistoryTTL', None)
CheckHistoryImportPeer = getattr(_fn, 'CheckHistoryImportPeer', getattr(_fn, 'MessagesCheckHistoryImportPeer', None))
MessagesCheckHistoryImportPeer = getattr(_fn, 'MessagesCheckHistoryImportPeer', None)
SetChatTheme = getattr(_fn, 'SetChatTheme', getattr(_fn, 'MessagesSetChatTheme', None))
MessagesSetChatTheme = getattr(_fn, 'MessagesSetChatTheme', None)
GetMessageReadParticipants = getattr(_fn, 'GetMessageReadParticipants', getattr(_fn, 'MessagesGetMessageReadParticipants', None))
MessagesGetMessageReadParticipants = getattr(_fn, 'MessagesGetMessageReadParticipants', None)
GetSearchResultsCalendar = getattr(_fn, 'GetSearchResultsCalendar', getattr(_fn, 'MessagesGetSearchResultsCalendar', None))
MessagesGetSearchResultsCalendar = getattr(_fn, 'MessagesGetSearchResultsCalendar', None)
GetSearchResultsPositions = getattr(_fn, 'GetSearchResultsPositions', getattr(_fn, 'MessagesGetSearchResultsPositions', None))
MessagesGetSearchResultsPositions = getattr(_fn, 'MessagesGetSearchResultsPositions', None)
HideChatJoinRequest = getattr(_fn, 'HideChatJoinRequest', getattr(_fn, 'MessagesHideChatJoinRequest', None))
MessagesHideChatJoinRequest = getattr(_fn, 'MessagesHideChatJoinRequest', None)
HideAllChatJoinRequests = getattr(_fn, 'HideAllChatJoinRequests', getattr(_fn, 'MessagesHideAllChatJoinRequests', None))
MessagesHideAllChatJoinRequests = getattr(_fn, 'MessagesHideAllChatJoinRequests', None)
ToggleNoForwards = getattr(_fn, 'ToggleNoForwards', getattr(_fn, 'MessagesToggleNoForwards', None))
MessagesToggleNoForwards = getattr(_fn, 'MessagesToggleNoForwards', None)
SaveDefaultSendAs = getattr(_fn, 'SaveDefaultSendAs', getattr(_fn, 'MessagesSaveDefaultSendAs', None))
MessagesSaveDefaultSendAs = getattr(_fn, 'MessagesSaveDefaultSendAs', None)
SendReaction = getattr(_fn, 'SendReaction', getattr(_fn, 'MessagesSendReaction', None))
MessagesSendReaction = getattr(_fn, 'MessagesSendReaction', None)
GetMessagesReactions = getattr(_fn, 'GetMessagesReactions', getattr(_fn, 'MessagesGetMessagesReactions', None))
MessagesGetMessagesReactions = getattr(_fn, 'MessagesGetMessagesReactions', None)
GetMessageReactionsList = getattr(_fn, 'GetMessageReactionsList', getattr(_fn, 'MessagesGetMessageReactionsList', None))
MessagesGetMessageReactionsList = getattr(_fn, 'MessagesGetMessageReactionsList', None)
SetChatAvailableReactions = getattr(_fn, 'SetChatAvailableReactions', getattr(_fn, 'MessagesSetChatAvailableReactions', None))
MessagesSetChatAvailableReactions = getattr(_fn, 'MessagesSetChatAvailableReactions', None)
GetAvailableReactions = getattr(_fn, 'GetAvailableReactions', getattr(_fn, 'MessagesGetAvailableReactions', None))
MessagesGetAvailableReactions = getattr(_fn, 'MessagesGetAvailableReactions', None)
SetDefaultReaction = getattr(_fn, 'SetDefaultReaction', getattr(_fn, 'MessagesSetDefaultReaction', None))
MessagesSetDefaultReaction = getattr(_fn, 'MessagesSetDefaultReaction', None)
TranslateText = getattr(_fn, 'TranslateText', getattr(_fn, 'MessagesTranslateText', None))
MessagesTranslateText = getattr(_fn, 'MessagesTranslateText', None)
GetUnreadReactions = getattr(_fn, 'GetUnreadReactions', getattr(_fn, 'MessagesGetUnreadReactions', None))
MessagesGetUnreadReactions = getattr(_fn, 'MessagesGetUnreadReactions', None)
ReadReactions = getattr(_fn, 'ReadReactions', getattr(_fn, 'MessagesReadReactions', None))
MessagesReadReactions = getattr(_fn, 'MessagesReadReactions', None)
SearchSentMedia = getattr(_fn, 'SearchSentMedia', getattr(_fn, 'MessagesSearchSentMedia', None))
MessagesSearchSentMedia = getattr(_fn, 'MessagesSearchSentMedia', None)
GetAttachMenuBots = getattr(_fn, 'GetAttachMenuBots', getattr(_fn, 'MessagesGetAttachMenuBots', None))
MessagesGetAttachMenuBots = getattr(_fn, 'MessagesGetAttachMenuBots', None)
GetAttachMenuBot = getattr(_fn, 'GetAttachMenuBot', getattr(_fn, 'MessagesGetAttachMenuBot', None))
MessagesGetAttachMenuBot = getattr(_fn, 'MessagesGetAttachMenuBot', None)
ToggleBotInAttachMenu = getattr(_fn, 'ToggleBotInAttachMenu', getattr(_fn, 'MessagesToggleBotInAttachMenu', None))
MessagesToggleBotInAttachMenu = getattr(_fn, 'MessagesToggleBotInAttachMenu', None)
RequestWebView = getattr(_fn, 'RequestWebView', getattr(_fn, 'MessagesRequestWebView', None))
MessagesRequestWebView = getattr(_fn, 'MessagesRequestWebView', None)
ProlongWebView = getattr(_fn, 'ProlongWebView', getattr(_fn, 'MessagesProlongWebView', None))
MessagesProlongWebView = getattr(_fn, 'MessagesProlongWebView', None)
RequestSimpleWebView = getattr(_fn, 'RequestSimpleWebView', getattr(_fn, 'MessagesRequestSimpleWebView', None))
MessagesRequestSimpleWebView = getattr(_fn, 'MessagesRequestSimpleWebView', None)
SendWebViewResultMessage = getattr(_fn, 'SendWebViewResultMessage', getattr(_fn, 'MessagesSendWebViewResultMessage', None))
MessagesSendWebViewResultMessage = getattr(_fn, 'MessagesSendWebViewResultMessage', None)
SendWebViewData = getattr(_fn, 'SendWebViewData', getattr(_fn, 'MessagesSendWebViewData', None))
MessagesSendWebViewData = getattr(_fn, 'MessagesSendWebViewData', None)
TranscribeAudio = getattr(_fn, 'TranscribeAudio', getattr(_fn, 'MessagesTranscribeAudio', None))
MessagesTranscribeAudio = getattr(_fn, 'MessagesTranscribeAudio', None)
RateTranscribedAudio = getattr(_fn, 'RateTranscribedAudio', getattr(_fn, 'MessagesRateTranscribedAudio', None))
MessagesRateTranscribedAudio = getattr(_fn, 'MessagesRateTranscribedAudio', None)
GetCustomEmojiDocuments = getattr(_fn, 'GetCustomEmojiDocuments', getattr(_fn, 'MessagesGetCustomEmojiDocuments', None))
MessagesGetCustomEmojiDocuments = getattr(_fn, 'MessagesGetCustomEmojiDocuments', None)
GetEmojiStickers = getattr(_fn, 'GetEmojiStickers', getattr(_fn, 'MessagesGetEmojiStickers', None))
MessagesGetEmojiStickers = getattr(_fn, 'MessagesGetEmojiStickers', None)
GetFeaturedEmojiStickers = getattr(_fn, 'GetFeaturedEmojiStickers', getattr(_fn, 'MessagesGetFeaturedEmojiStickers', None))
MessagesGetFeaturedEmojiStickers = getattr(_fn, 'MessagesGetFeaturedEmojiStickers', None)
ReportReaction = getattr(_fn, 'ReportReaction', getattr(_fn, 'MessagesReportReaction', None))
MessagesReportReaction = getattr(_fn, 'MessagesReportReaction', None)
GetTopReactions = getattr(_fn, 'GetTopReactions', getattr(_fn, 'MessagesGetTopReactions', None))
MessagesGetTopReactions = getattr(_fn, 'MessagesGetTopReactions', None)
GetRecentReactions = getattr(_fn, 'GetRecentReactions', getattr(_fn, 'MessagesGetRecentReactions', None))
MessagesGetRecentReactions = getattr(_fn, 'MessagesGetRecentReactions', None)
ClearRecentReactions = getattr(_fn, 'ClearRecentReactions', getattr(_fn, 'MessagesClearRecentReactions', None))
MessagesClearRecentReactions = getattr(_fn, 'MessagesClearRecentReactions', None)
GetExtendedMedia = getattr(_fn, 'GetExtendedMedia', getattr(_fn, 'MessagesGetExtendedMedia', None))
MessagesGetExtendedMedia = getattr(_fn, 'MessagesGetExtendedMedia', None)
SetDefaultHistoryTTL = getattr(_fn, 'SetDefaultHistoryTTL', getattr(_fn, 'MessagesSetDefaultHistoryTTL', None))
MessagesSetDefaultHistoryTTL = getattr(_fn, 'MessagesSetDefaultHistoryTTL', None)
GetDefaultHistoryTTL = getattr(_fn, 'GetDefaultHistoryTTL', getattr(_fn, 'MessagesGetDefaultHistoryTTL', None))
MessagesGetDefaultHistoryTTL = getattr(_fn, 'MessagesGetDefaultHistoryTTL', None)
SendBotRequestedPeer = getattr(_fn, 'SendBotRequestedPeer', getattr(_fn, 'MessagesSendBotRequestedPeer', None))
MessagesSendBotRequestedPeer = getattr(_fn, 'MessagesSendBotRequestedPeer', None)
GetEmojiGroups = getattr(_fn, 'GetEmojiGroups', getattr(_fn, 'MessagesGetEmojiGroups', None))
MessagesGetEmojiGroups = getattr(_fn, 'MessagesGetEmojiGroups', None)
GetEmojiStatusGroups = getattr(_fn, 'GetEmojiStatusGroups', getattr(_fn, 'MessagesGetEmojiStatusGroups', None))
MessagesGetEmojiStatusGroups = getattr(_fn, 'MessagesGetEmojiStatusGroups', None)
GetEmojiProfilePhotoGroups = getattr(_fn, 'GetEmojiProfilePhotoGroups', getattr(_fn, 'MessagesGetEmojiProfilePhotoGroups', None))
MessagesGetEmojiProfilePhotoGroups = getattr(_fn, 'MessagesGetEmojiProfilePhotoGroups', None)
SearchCustomEmoji = getattr(_fn, 'SearchCustomEmoji', getattr(_fn, 'MessagesSearchCustomEmoji', None))
MessagesSearchCustomEmoji = getattr(_fn, 'MessagesSearchCustomEmoji', None)
TogglePeerTranslations = getattr(_fn, 'TogglePeerTranslations', getattr(_fn, 'MessagesTogglePeerTranslations', None))
MessagesTogglePeerTranslations = getattr(_fn, 'MessagesTogglePeerTranslations', None)
GetBotApp = getattr(_fn, 'GetBotApp', getattr(_fn, 'MessagesGetBotApp', None))
MessagesGetBotApp = getattr(_fn, 'MessagesGetBotApp', None)
RequestAppWebView = getattr(_fn, 'RequestAppWebView', getattr(_fn, 'MessagesRequestAppWebView', None))
MessagesRequestAppWebView = getattr(_fn, 'MessagesRequestAppWebView', None)
SetChatWallPaper = getattr(_fn, 'SetChatWallPaper', getattr(_fn, 'MessagesSetChatWallPaper', None))
MessagesSetChatWallPaper = getattr(_fn, 'MessagesSetChatWallPaper', None)
SearchEmojiStickerSets = getattr(_fn, 'SearchEmojiStickerSets', getattr(_fn, 'MessagesSearchEmojiStickerSets', None))
MessagesSearchEmojiStickerSets = getattr(_fn, 'MessagesSearchEmojiStickerSets', None)
GetSavedDialogs = getattr(_fn, 'GetSavedDialogs', getattr(_fn, 'MessagesGetSavedDialogs', None))
MessagesGetSavedDialogs = getattr(_fn, 'MessagesGetSavedDialogs', None)
GetSavedHistory = getattr(_fn, 'GetSavedHistory', getattr(_fn, 'MessagesGetSavedHistory', None))
MessagesGetSavedHistory = getattr(_fn, 'MessagesGetSavedHistory', None)
DeleteSavedHistory = getattr(_fn, 'DeleteSavedHistory', getattr(_fn, 'MessagesDeleteSavedHistory', None))
MessagesDeleteSavedHistory = getattr(_fn, 'MessagesDeleteSavedHistory', None)
GetPinnedSavedDialogs = getattr(_fn, 'GetPinnedSavedDialogs', getattr(_fn, 'MessagesGetPinnedSavedDialogs', None))
MessagesGetPinnedSavedDialogs = getattr(_fn, 'MessagesGetPinnedSavedDialogs', None)
ToggleSavedDialogPin = getattr(_fn, 'ToggleSavedDialogPin', getattr(_fn, 'MessagesToggleSavedDialogPin', None))
MessagesToggleSavedDialogPin = getattr(_fn, 'MessagesToggleSavedDialogPin', None)
ReorderPinnedSavedDialogs = getattr(_fn, 'ReorderPinnedSavedDialogs', getattr(_fn, 'MessagesReorderPinnedSavedDialogs', None))
MessagesReorderPinnedSavedDialogs = getattr(_fn, 'MessagesReorderPinnedSavedDialogs', None)
GetSavedReactionTags = getattr(_fn, 'GetSavedReactionTags', getattr(_fn, 'MessagesGetSavedReactionTags', None))
MessagesGetSavedReactionTags = getattr(_fn, 'MessagesGetSavedReactionTags', None)
UpdateSavedReactionTag = getattr(_fn, 'UpdateSavedReactionTag', getattr(_fn, 'MessagesUpdateSavedReactionTag', None))
MessagesUpdateSavedReactionTag = getattr(_fn, 'MessagesUpdateSavedReactionTag', None)
GetDefaultTagReactions = getattr(_fn, 'GetDefaultTagReactions', getattr(_fn, 'MessagesGetDefaultTagReactions', None))
MessagesGetDefaultTagReactions = getattr(_fn, 'MessagesGetDefaultTagReactions', None)
GetOutboxReadDate = getattr(_fn, 'GetOutboxReadDate', getattr(_fn, 'MessagesGetOutboxReadDate', None))
MessagesGetOutboxReadDate = getattr(_fn, 'MessagesGetOutboxReadDate', None)
GetQuickReplies = getattr(_fn, 'GetQuickReplies', getattr(_fn, 'MessagesGetQuickReplies', None))
MessagesGetQuickReplies = getattr(_fn, 'MessagesGetQuickReplies', None)
ReorderQuickReplies = getattr(_fn, 'ReorderQuickReplies', getattr(_fn, 'MessagesReorderQuickReplies', None))
MessagesReorderQuickReplies = getattr(_fn, 'MessagesReorderQuickReplies', None)
CheckQuickReplyShortcut = getattr(_fn, 'CheckQuickReplyShortcut', getattr(_fn, 'MessagesCheckQuickReplyShortcut', None))
MessagesCheckQuickReplyShortcut = getattr(_fn, 'MessagesCheckQuickReplyShortcut', None)
EditQuickReplyShortcut = getattr(_fn, 'EditQuickReplyShortcut', getattr(_fn, 'MessagesEditQuickReplyShortcut', None))
MessagesEditQuickReplyShortcut = getattr(_fn, 'MessagesEditQuickReplyShortcut', None)
DeleteQuickReplyShortcut = getattr(_fn, 'DeleteQuickReplyShortcut', getattr(_fn, 'MessagesDeleteQuickReplyShortcut', None))
MessagesDeleteQuickReplyShortcut = getattr(_fn, 'MessagesDeleteQuickReplyShortcut', None)
GetQuickReplyMessages = getattr(_fn, 'GetQuickReplyMessages', getattr(_fn, 'MessagesGetQuickReplyMessages', None))
MessagesGetQuickReplyMessages = getattr(_fn, 'MessagesGetQuickReplyMessages', None)
SendQuickReplyMessages = getattr(_fn, 'SendQuickReplyMessages', getattr(_fn, 'MessagesSendQuickReplyMessages', None))
MessagesSendQuickReplyMessages = getattr(_fn, 'MessagesSendQuickReplyMessages', None)
DeleteQuickReplyMessages = getattr(_fn, 'DeleteQuickReplyMessages', getattr(_fn, 'MessagesDeleteQuickReplyMessages', None))
MessagesDeleteQuickReplyMessages = getattr(_fn, 'MessagesDeleteQuickReplyMessages', None)
ToggleDialogFilterTags = getattr(_fn, 'ToggleDialogFilterTags', getattr(_fn, 'MessagesToggleDialogFilterTags', None))
MessagesToggleDialogFilterTags = getattr(_fn, 'MessagesToggleDialogFilterTags', None)
GetMyStickers = getattr(_fn, 'GetMyStickers', getattr(_fn, 'MessagesGetMyStickers', None))
MessagesGetMyStickers = getattr(_fn, 'MessagesGetMyStickers', None)
GetEmojiStickerGroups = getattr(_fn, 'GetEmojiStickerGroups', getattr(_fn, 'MessagesGetEmojiStickerGroups', None))
MessagesGetEmojiStickerGroups = getattr(_fn, 'MessagesGetEmojiStickerGroups', None)
GetAvailableEffects = getattr(_fn, 'GetAvailableEffects', getattr(_fn, 'MessagesGetAvailableEffects', None))
MessagesGetAvailableEffects = getattr(_fn, 'MessagesGetAvailableEffects', None)
EditFactCheck = getattr(_fn, 'EditFactCheck', getattr(_fn, 'MessagesEditFactCheck', None))
MessagesEditFactCheck = getattr(_fn, 'MessagesEditFactCheck', None)
DeleteFactCheck = getattr(_fn, 'DeleteFactCheck', getattr(_fn, 'MessagesDeleteFactCheck', None))
MessagesDeleteFactCheck = getattr(_fn, 'MessagesDeleteFactCheck', None)
GetFactCheck = getattr(_fn, 'GetFactCheck', getattr(_fn, 'MessagesGetFactCheck', None))
MessagesGetFactCheck = getattr(_fn, 'MessagesGetFactCheck', None)
RequestMainWebView = getattr(_fn, 'RequestMainWebView', getattr(_fn, 'MessagesRequestMainWebView', None))
MessagesRequestMainWebView = getattr(_fn, 'MessagesRequestMainWebView', None)
SendPaidReaction = getattr(_fn, 'SendPaidReaction', getattr(_fn, 'MessagesSendPaidReaction', None))
MessagesSendPaidReaction = getattr(_fn, 'MessagesSendPaidReaction', None)
TogglePaidReactionPrivacy = getattr(_fn, 'TogglePaidReactionPrivacy', getattr(_fn, 'MessagesTogglePaidReactionPrivacy', None))
MessagesTogglePaidReactionPrivacy = getattr(_fn, 'MessagesTogglePaidReactionPrivacy', None)
GetPaidReactionPrivacy = getattr(_fn, 'GetPaidReactionPrivacy', getattr(_fn, 'MessagesGetPaidReactionPrivacy', None))
MessagesGetPaidReactionPrivacy = getattr(_fn, 'MessagesGetPaidReactionPrivacy', None)
ViewSponsoredMessage = getattr(_fn, 'ViewSponsoredMessage', getattr(_fn, 'MessagesViewSponsoredMessage', None))
MessagesViewSponsoredMessage = getattr(_fn, 'MessagesViewSponsoredMessage', None)
ClickSponsoredMessage = getattr(_fn, 'ClickSponsoredMessage', getattr(_fn, 'MessagesClickSponsoredMessage', None))
MessagesClickSponsoredMessage = getattr(_fn, 'MessagesClickSponsoredMessage', None)
ReportSponsoredMessage = getattr(_fn, 'ReportSponsoredMessage', getattr(_fn, 'MessagesReportSponsoredMessage', None))
MessagesReportSponsoredMessage = getattr(_fn, 'MessagesReportSponsoredMessage', None)
GetSponsoredMessages = getattr(_fn, 'GetSponsoredMessages', getattr(_fn, 'MessagesGetSponsoredMessages', None))
MessagesGetSponsoredMessages = getattr(_fn, 'MessagesGetSponsoredMessages', None)
SavePreparedInlineMessage = getattr(_fn, 'SavePreparedInlineMessage', getattr(_fn, 'MessagesSavePreparedInlineMessage', None))
MessagesSavePreparedInlineMessage = getattr(_fn, 'MessagesSavePreparedInlineMessage', None)
GetPreparedInlineMessage = getattr(_fn, 'GetPreparedInlineMessage', getattr(_fn, 'MessagesGetPreparedInlineMessage', None))
MessagesGetPreparedInlineMessage = getattr(_fn, 'MessagesGetPreparedInlineMessage', None)
SearchStickers = getattr(_fn, 'SearchStickers', getattr(_fn, 'MessagesSearchStickers', None))
MessagesSearchStickers = getattr(_fn, 'MessagesSearchStickers', None)
ReportMessagesDelivery = getattr(_fn, 'ReportMessagesDelivery', getattr(_fn, 'MessagesReportMessagesDelivery', None))
MessagesReportMessagesDelivery = getattr(_fn, 'MessagesReportMessagesDelivery', None)
GetSavedDialogsByID = getattr(_fn, 'GetSavedDialogsByID', getattr(_fn, 'MessagesGetSavedDialogsByID', None))
MessagesGetSavedDialogsByID = getattr(_fn, 'MessagesGetSavedDialogsByID', None)
ReadSavedHistory = getattr(_fn, 'ReadSavedHistory', getattr(_fn, 'MessagesReadSavedHistory', None))
MessagesReadSavedHistory = getattr(_fn, 'MessagesReadSavedHistory', None)
ToggleTodoCompleted = getattr(_fn, 'ToggleTodoCompleted', getattr(_fn, 'MessagesToggleTodoCompleted', None))
MessagesToggleTodoCompleted = getattr(_fn, 'MessagesToggleTodoCompleted', None)
AppendTodoList = getattr(_fn, 'AppendTodoList', getattr(_fn, 'MessagesAppendTodoList', None))
MessagesAppendTodoList = getattr(_fn, 'MessagesAppendTodoList', None)
ToggleSuggestedPostApproval = getattr(_fn, 'ToggleSuggestedPostApproval', getattr(_fn, 'MessagesToggleSuggestedPostApproval', None))
MessagesToggleSuggestedPostApproval = getattr(_fn, 'MessagesToggleSuggestedPostApproval', None)
GetForumTopics = getattr(_fn, 'GetForumTopics', getattr(_fn, 'MessagesGetForumTopics', None))
MessagesGetForumTopics = getattr(_fn, 'MessagesGetForumTopics', None)
GetForumTopicsByID = getattr(_fn, 'GetForumTopicsByID', getattr(_fn, 'MessagesGetForumTopicsByID', None))
MessagesGetForumTopicsByID = getattr(_fn, 'MessagesGetForumTopicsByID', None)
EditForumTopic = getattr(_fn, 'EditForumTopic', getattr(_fn, 'MessagesEditForumTopic', None))
MessagesEditForumTopic = getattr(_fn, 'MessagesEditForumTopic', None)
UpdatePinnedForumTopic = getattr(_fn, 'UpdatePinnedForumTopic', getattr(_fn, 'MessagesUpdatePinnedForumTopic', None))
MessagesUpdatePinnedForumTopic = getattr(_fn, 'MessagesUpdatePinnedForumTopic', None)
ReorderPinnedForumTopics = getattr(_fn, 'ReorderPinnedForumTopics', getattr(_fn, 'MessagesReorderPinnedForumTopics', None))
MessagesReorderPinnedForumTopics = getattr(_fn, 'MessagesReorderPinnedForumTopics', None)
CreateForumTopic = getattr(_fn, 'CreateForumTopic', getattr(_fn, 'MessagesCreateForumTopic', None))
MessagesCreateForumTopic = getattr(_fn, 'MessagesCreateForumTopic', None)
DeleteTopicHistory = getattr(_fn, 'DeleteTopicHistory', getattr(_fn, 'MessagesDeleteTopicHistory', None))
MessagesDeleteTopicHistory = getattr(_fn, 'MessagesDeleteTopicHistory', None)
GetEmojiGameInfo = getattr(_fn, 'GetEmojiGameInfo', getattr(_fn, 'MessagesGetEmojiGameInfo', None))
MessagesGetEmojiGameInfo = getattr(_fn, 'MessagesGetEmojiGameInfo', None)
SummarizeText = getattr(_fn, 'SummarizeText', getattr(_fn, 'MessagesSummarizeText', None))
MessagesSummarizeText = getattr(_fn, 'MessagesSummarizeText', None)
EditChatCreator = getattr(_fn, 'EditChatCreator', getattr(_fn, 'MessagesEditChatCreator', None))
MessagesEditChatCreator = getattr(_fn, 'MessagesEditChatCreator', None)
GetFutureChatCreatorAfterLeave = getattr(_fn, 'GetFutureChatCreatorAfterLeave', getattr(_fn, 'MessagesGetFutureChatCreatorAfterLeave', None))
MessagesGetFutureChatCreatorAfterLeave = getattr(_fn, 'MessagesGetFutureChatCreatorAfterLeave', None)
EditChatParticipantRank = getattr(_fn, 'EditChatParticipantRank', getattr(_fn, 'MessagesEditChatParticipantRank', None))
MessagesEditChatParticipantRank = getattr(_fn, 'MessagesEditChatParticipantRank', None)
DeclineUrlAuth = getattr(_fn, 'DeclineUrlAuth', getattr(_fn, 'MessagesDeclineUrlAuth', None))
MessagesDeclineUrlAuth = getattr(_fn, 'MessagesDeclineUrlAuth', None)
CheckUrlAuthMatchCode = getattr(_fn, 'CheckUrlAuthMatchCode', getattr(_fn, 'MessagesCheckUrlAuthMatchCode', None))
MessagesCheckUrlAuthMatchCode = getattr(_fn, 'MessagesCheckUrlAuthMatchCode', None)
ComposeMessageWithAI = getattr(_fn, 'ComposeMessageWithAI', getattr(_fn, 'MessagesComposeMessageWithAI', None))
MessagesComposeMessageWithAI = getattr(_fn, 'MessagesComposeMessageWithAI', None)
ReportReadMetrics = getattr(_fn, 'ReportReadMetrics', getattr(_fn, 'MessagesReportReadMetrics', None))
MessagesReportReadMetrics = getattr(_fn, 'MessagesReportReadMetrics', None)
ReportMusicListen = getattr(_fn, 'ReportMusicListen', getattr(_fn, 'MessagesReportMusicListen', None))
MessagesReportMusicListen = getattr(_fn, 'MessagesReportMusicListen', None)
AddPollAnswer = getattr(_fn, 'AddPollAnswer', getattr(_fn, 'MessagesAddPollAnswer', None))
MessagesAddPollAnswer = getattr(_fn, 'MessagesAddPollAnswer', None)
DeletePollAnswer = getattr(_fn, 'DeletePollAnswer', getattr(_fn, 'MessagesDeletePollAnswer', None))
MessagesDeletePollAnswer = getattr(_fn, 'MessagesDeletePollAnswer', None)
GetUnreadPollVotes = getattr(_fn, 'GetUnreadPollVotes', getattr(_fn, 'MessagesGetUnreadPollVotes', None))
MessagesGetUnreadPollVotes = getattr(_fn, 'MessagesGetUnreadPollVotes', None)
ReadPollVotes = getattr(_fn, 'ReadPollVotes', getattr(_fn, 'MessagesReadPollVotes', None))
MessagesReadPollVotes = getattr(_fn, 'MessagesReadPollVotes', None)
SetBotGuestChatResult = getattr(_fn, 'SetBotGuestChatResult', getattr(_fn, 'MessagesSetBotGuestChatResult', None))
MessagesSetBotGuestChatResult = getattr(_fn, 'MessagesSetBotGuestChatResult', None)
DeleteParticipantReactions = getattr(_fn, 'DeleteParticipantReactions', getattr(_fn, 'MessagesDeleteParticipantReactions', None))
MessagesDeleteParticipantReactions = getattr(_fn, 'MessagesDeleteParticipantReactions', None)
DeleteParticipantReaction = getattr(_fn, 'DeleteParticipantReaction', getattr(_fn, 'MessagesDeleteParticipantReaction', None))
MessagesDeleteParticipantReaction = getattr(_fn, 'MessagesDeleteParticipantReaction', None)
GetPersonalChannelHistory = getattr(_fn, 'GetPersonalChannelHistory', getattr(_fn, 'MessagesGetPersonalChannelHistory', None))
MessagesGetPersonalChannelHistory = getattr(_fn, 'MessagesGetPersonalChannelHistory', None)

__all__ = [
    "GetMessages",
    "MessagesGetMessages",
    "GetDialogs",
    "MessagesGetDialogs",
    "GetHistory",
    "MessagesGetHistory",
    "Search",
    "MessagesSearch",
    "ReadHistory",
    "MessagesReadHistory",
    "DeleteHistory",
    "MessagesDeleteHistory",
    "DeleteMessages",
    "MessagesDeleteMessages",
    "ReceivedMessages",
    "MessagesReceivedMessages",
    "SetTyping",
    "MessagesSetTyping",
    "SendMessage",
    "MessagesSendMessage",
    "SendMedia",
    "MessagesSendMedia",
    "ForwardMessages",
    "MessagesForwardMessages",
    "ReportSpam",
    "MessagesReportSpam",
    "GetPeerSettings",
    "MessagesGetPeerSettings",
    "Report",
    "MessagesReport",
    "GetChats",
    "MessagesGetChats",
    "GetFullChat",
    "MessagesGetFullChat",
    "EditChatTitle",
    "MessagesEditChatTitle",
    "EditChatPhoto",
    "MessagesEditChatPhoto",
    "AddChatUser",
    "MessagesAddChatUser",
    "DeleteChatUser",
    "MessagesDeleteChatUser",
    "CreateChat",
    "MessagesCreateChat",
    "GetDhConfig",
    "MessagesGetDhConfig",
    "RequestEncryption",
    "MessagesRequestEncryption",
    "AcceptEncryption",
    "MessagesAcceptEncryption",
    "DiscardEncryption",
    "MessagesDiscardEncryption",
    "SetEncryptedTyping",
    "MessagesSetEncryptedTyping",
    "ReadEncryptedHistory",
    "MessagesReadEncryptedHistory",
    "SendEncrypted",
    "MessagesSendEncrypted",
    "SendEncryptedFile",
    "MessagesSendEncryptedFile",
    "SendEncryptedService",
    "MessagesSendEncryptedService",
    "ReceivedQueue",
    "MessagesReceivedQueue",
    "ReportEncryptedSpam",
    "MessagesReportEncryptedSpam",
    "ReadMessageContents",
    "MessagesReadMessageContents",
    "GetStickers",
    "MessagesGetStickers",
    "GetAllStickers",
    "MessagesGetAllStickers",
    "GetWebPagePreview",
    "MessagesGetWebPagePreview",
    "ExportChatInvite",
    "MessagesExportChatInvite",
    "CheckChatInvite",
    "MessagesCheckChatInvite",
    "ImportChatInvite",
    "MessagesImportChatInvite",
    "GetStickerSet",
    "MessagesGetStickerSet",
    "InstallStickerSet",
    "MessagesInstallStickerSet",
    "UninstallStickerSet",
    "MessagesUninstallStickerSet",
    "StartBot",
    "MessagesStartBot",
    "GetMessagesViews",
    "MessagesGetMessagesViews",
    "EditChatAdmin",
    "MessagesEditChatAdmin",
    "MigrateChat",
    "MessagesMigrateChat",
    "SearchGlobal",
    "MessagesSearchGlobal",
    "ReorderStickerSets",
    "MessagesReorderStickerSets",
    "GetDocumentByHash",
    "MessagesGetDocumentByHash",
    "GetSavedGifs",
    "MessagesGetSavedGifs",
    "SaveGif",
    "MessagesSaveGif",
    "GetInlineBotResults",
    "MessagesGetInlineBotResults",
    "SetInlineBotResults",
    "MessagesSetInlineBotResults",
    "SendInlineBotResult",
    "MessagesSendInlineBotResult",
    "GetMessageEditData",
    "MessagesGetMessageEditData",
    "EditMessage",
    "MessagesEditMessage",
    "EditInlineBotMessage",
    "MessagesEditInlineBotMessage",
    "GetBotCallbackAnswer",
    "MessagesGetBotCallbackAnswer",
    "SetBotCallbackAnswer",
    "MessagesSetBotCallbackAnswer",
    "GetPeerDialogs",
    "MessagesGetPeerDialogs",
    "SaveDraft",
    "MessagesSaveDraft",
    "GetAllDrafts",
    "MessagesGetAllDrafts",
    "GetFeaturedStickers",
    "MessagesGetFeaturedStickers",
    "ReadFeaturedStickers",
    "MessagesReadFeaturedStickers",
    "GetRecentStickers",
    "MessagesGetRecentStickers",
    "SaveRecentSticker",
    "MessagesSaveRecentSticker",
    "ClearRecentStickers",
    "MessagesClearRecentStickers",
    "GetArchivedStickers",
    "MessagesGetArchivedStickers",
    "GetMaskStickers",
    "MessagesGetMaskStickers",
    "GetAttachedStickers",
    "MessagesGetAttachedStickers",
    "SetGameScore",
    "MessagesSetGameScore",
    "SetInlineGameScore",
    "MessagesSetInlineGameScore",
    "GetGameHighScores",
    "MessagesGetGameHighScores",
    "GetInlineGameHighScores",
    "MessagesGetInlineGameHighScores",
    "GetCommonChats",
    "MessagesGetCommonChats",
    "GetWebPage",
    "MessagesGetWebPage",
    "ToggleDialogPin",
    "MessagesToggleDialogPin",
    "ReorderPinnedDialogs",
    "MessagesReorderPinnedDialogs",
    "GetPinnedDialogs",
    "MessagesGetPinnedDialogs",
    "SetBotShippingResults",
    "MessagesSetBotShippingResults",
    "SetBotPrecheckoutResults",
    "MessagesSetBotPrecheckoutResults",
    "UploadMedia",
    "MessagesUploadMedia",
    "SendScreenshotNotification",
    "MessagesSendScreenshotNotification",
    "GetFavedStickers",
    "MessagesGetFavedStickers",
    "FaveSticker",
    "MessagesFaveSticker",
    "GetUnreadMentions",
    "MessagesGetUnreadMentions",
    "ReadMentions",
    "MessagesReadMentions",
    "GetRecentLocations",
    "MessagesGetRecentLocations",
    "SendMultiMedia",
    "MessagesSendMultiMedia",
    "UploadEncryptedFile",
    "MessagesUploadEncryptedFile",
    "SearchStickerSets",
    "MessagesSearchStickerSets",
    "GetSplitRanges",
    "MessagesGetSplitRanges",
    "MarkDialogUnread",
    "MessagesMarkDialogUnread",
    "GetDialogUnreadMarks",
    "MessagesGetDialogUnreadMarks",
    "ClearAllDrafts",
    "MessagesClearAllDrafts",
    "UpdatePinnedMessage",
    "MessagesUpdatePinnedMessage",
    "SendVote",
    "MessagesSendVote",
    "GetPollResults",
    "MessagesGetPollResults",
    "GetOnlines",
    "MessagesGetOnlines",
    "EditChatAbout",
    "MessagesEditChatAbout",
    "EditChatDefaultBannedRights",
    "MessagesEditChatDefaultBannedRights",
    "GetEmojiKeywords",
    "MessagesGetEmojiKeywords",
    "GetEmojiKeywordsDifference",
    "MessagesGetEmojiKeywordsDifference",
    "GetEmojiKeywordsLanguages",
    "MessagesGetEmojiKeywordsLanguages",
    "GetEmojiURL",
    "MessagesGetEmojiURL",
    "GetSearchCounters",
    "MessagesGetSearchCounters",
    "RequestUrlAuth",
    "MessagesRequestUrlAuth",
    "AcceptUrlAuth",
    "MessagesAcceptUrlAuth",
    "HidePeerSettingsBar",
    "MessagesHidePeerSettingsBar",
    "GetScheduledHistory",
    "MessagesGetScheduledHistory",
    "GetScheduledMessages",
    "MessagesGetScheduledMessages",
    "SendScheduledMessages",
    "MessagesSendScheduledMessages",
    "DeleteScheduledMessages",
    "MessagesDeleteScheduledMessages",
    "GetPollVotes",
    "MessagesGetPollVotes",
    "ToggleStickerSets",
    "MessagesToggleStickerSets",
    "GetDialogFilters",
    "MessagesGetDialogFilters",
    "GetSuggestedDialogFilters",
    "MessagesGetSuggestedDialogFilters",
    "UpdateDialogFilter",
    "MessagesUpdateDialogFilter",
    "UpdateDialogFiltersOrder",
    "MessagesUpdateDialogFiltersOrder",
    "GetOldFeaturedStickers",
    "MessagesGetOldFeaturedStickers",
    "GetReplies",
    "MessagesGetReplies",
    "GetDiscussionMessage",
    "MessagesGetDiscussionMessage",
    "ReadDiscussion",
    "MessagesReadDiscussion",
    "UnpinAllMessages",
    "MessagesUnpinAllMessages",
    "DeleteChat",
    "MessagesDeleteChat",
    "DeletePhoneCallHistory",
    "MessagesDeletePhoneCallHistory",
    "CheckHistoryImport",
    "MessagesCheckHistoryImport",
    "InitHistoryImport",
    "MessagesInitHistoryImport",
    "UploadImportedMedia",
    "MessagesUploadImportedMedia",
    "StartHistoryImport",
    "MessagesStartHistoryImport",
    "GetExportedChatInvites",
    "MessagesGetExportedChatInvites",
    "GetExportedChatInvite",
    "MessagesGetExportedChatInvite",
    "EditExportedChatInvite",
    "MessagesEditExportedChatInvite",
    "DeleteRevokedExportedChatInvites",
    "MessagesDeleteRevokedExportedChatInvites",
    "DeleteExportedChatInvite",
    "MessagesDeleteExportedChatInvite",
    "GetAdminsWithInvites",
    "MessagesGetAdminsWithInvites",
    "GetChatInviteImporters",
    "MessagesGetChatInviteImporters",
    "SetHistoryTTL",
    "MessagesSetHistoryTTL",
    "CheckHistoryImportPeer",
    "MessagesCheckHistoryImportPeer",
    "SetChatTheme",
    "MessagesSetChatTheme",
    "GetMessageReadParticipants",
    "MessagesGetMessageReadParticipants",
    "GetSearchResultsCalendar",
    "MessagesGetSearchResultsCalendar",
    "GetSearchResultsPositions",
    "MessagesGetSearchResultsPositions",
    "HideChatJoinRequest",
    "MessagesHideChatJoinRequest",
    "HideAllChatJoinRequests",
    "MessagesHideAllChatJoinRequests",
    "ToggleNoForwards",
    "MessagesToggleNoForwards",
    "SaveDefaultSendAs",
    "MessagesSaveDefaultSendAs",
    "SendReaction",
    "MessagesSendReaction",
    "GetMessagesReactions",
    "MessagesGetMessagesReactions",
    "GetMessageReactionsList",
    "MessagesGetMessageReactionsList",
    "SetChatAvailableReactions",
    "MessagesSetChatAvailableReactions",
    "GetAvailableReactions",
    "MessagesGetAvailableReactions",
    "SetDefaultReaction",
    "MessagesSetDefaultReaction",
    "TranslateText",
    "MessagesTranslateText",
    "GetUnreadReactions",
    "MessagesGetUnreadReactions",
    "ReadReactions",
    "MessagesReadReactions",
    "SearchSentMedia",
    "MessagesSearchSentMedia",
    "GetAttachMenuBots",
    "MessagesGetAttachMenuBots",
    "GetAttachMenuBot",
    "MessagesGetAttachMenuBot",
    "ToggleBotInAttachMenu",
    "MessagesToggleBotInAttachMenu",
    "RequestWebView",
    "MessagesRequestWebView",
    "ProlongWebView",
    "MessagesProlongWebView",
    "RequestSimpleWebView",
    "MessagesRequestSimpleWebView",
    "SendWebViewResultMessage",
    "MessagesSendWebViewResultMessage",
    "SendWebViewData",
    "MessagesSendWebViewData",
    "TranscribeAudio",
    "MessagesTranscribeAudio",
    "RateTranscribedAudio",
    "MessagesRateTranscribedAudio",
    "GetCustomEmojiDocuments",
    "MessagesGetCustomEmojiDocuments",
    "GetEmojiStickers",
    "MessagesGetEmojiStickers",
    "GetFeaturedEmojiStickers",
    "MessagesGetFeaturedEmojiStickers",
    "ReportReaction",
    "MessagesReportReaction",
    "GetTopReactions",
    "MessagesGetTopReactions",
    "GetRecentReactions",
    "MessagesGetRecentReactions",
    "ClearRecentReactions",
    "MessagesClearRecentReactions",
    "GetExtendedMedia",
    "MessagesGetExtendedMedia",
    "SetDefaultHistoryTTL",
    "MessagesSetDefaultHistoryTTL",
    "GetDefaultHistoryTTL",
    "MessagesGetDefaultHistoryTTL",
    "SendBotRequestedPeer",
    "MessagesSendBotRequestedPeer",
    "GetEmojiGroups",
    "MessagesGetEmojiGroups",
    "GetEmojiStatusGroups",
    "MessagesGetEmojiStatusGroups",
    "GetEmojiProfilePhotoGroups",
    "MessagesGetEmojiProfilePhotoGroups",
    "SearchCustomEmoji",
    "MessagesSearchCustomEmoji",
    "TogglePeerTranslations",
    "MessagesTogglePeerTranslations",
    "GetBotApp",
    "MessagesGetBotApp",
    "RequestAppWebView",
    "MessagesRequestAppWebView",
    "SetChatWallPaper",
    "MessagesSetChatWallPaper",
    "SearchEmojiStickerSets",
    "MessagesSearchEmojiStickerSets",
    "GetSavedDialogs",
    "MessagesGetSavedDialogs",
    "GetSavedHistory",
    "MessagesGetSavedHistory",
    "DeleteSavedHistory",
    "MessagesDeleteSavedHistory",
    "GetPinnedSavedDialogs",
    "MessagesGetPinnedSavedDialogs",
    "ToggleSavedDialogPin",
    "MessagesToggleSavedDialogPin",
    "ReorderPinnedSavedDialogs",
    "MessagesReorderPinnedSavedDialogs",
    "GetSavedReactionTags",
    "MessagesGetSavedReactionTags",
    "UpdateSavedReactionTag",
    "MessagesUpdateSavedReactionTag",
    "GetDefaultTagReactions",
    "MessagesGetDefaultTagReactions",
    "GetOutboxReadDate",
    "MessagesGetOutboxReadDate",
    "GetQuickReplies",
    "MessagesGetQuickReplies",
    "ReorderQuickReplies",
    "MessagesReorderQuickReplies",
    "CheckQuickReplyShortcut",
    "MessagesCheckQuickReplyShortcut",
    "EditQuickReplyShortcut",
    "MessagesEditQuickReplyShortcut",
    "DeleteQuickReplyShortcut",
    "MessagesDeleteQuickReplyShortcut",
    "GetQuickReplyMessages",
    "MessagesGetQuickReplyMessages",
    "SendQuickReplyMessages",
    "MessagesSendQuickReplyMessages",
    "DeleteQuickReplyMessages",
    "MessagesDeleteQuickReplyMessages",
    "ToggleDialogFilterTags",
    "MessagesToggleDialogFilterTags",
    "GetMyStickers",
    "MessagesGetMyStickers",
    "GetEmojiStickerGroups",
    "MessagesGetEmojiStickerGroups",
    "GetAvailableEffects",
    "MessagesGetAvailableEffects",
    "EditFactCheck",
    "MessagesEditFactCheck",
    "DeleteFactCheck",
    "MessagesDeleteFactCheck",
    "GetFactCheck",
    "MessagesGetFactCheck",
    "RequestMainWebView",
    "MessagesRequestMainWebView",
    "SendPaidReaction",
    "MessagesSendPaidReaction",
    "TogglePaidReactionPrivacy",
    "MessagesTogglePaidReactionPrivacy",
    "GetPaidReactionPrivacy",
    "MessagesGetPaidReactionPrivacy",
    "ViewSponsoredMessage",
    "MessagesViewSponsoredMessage",
    "ClickSponsoredMessage",
    "MessagesClickSponsoredMessage",
    "ReportSponsoredMessage",
    "MessagesReportSponsoredMessage",
    "GetSponsoredMessages",
    "MessagesGetSponsoredMessages",
    "SavePreparedInlineMessage",
    "MessagesSavePreparedInlineMessage",
    "GetPreparedInlineMessage",
    "MessagesGetPreparedInlineMessage",
    "SearchStickers",
    "MessagesSearchStickers",
    "ReportMessagesDelivery",
    "MessagesReportMessagesDelivery",
    "GetSavedDialogsByID",
    "MessagesGetSavedDialogsByID",
    "ReadSavedHistory",
    "MessagesReadSavedHistory",
    "ToggleTodoCompleted",
    "MessagesToggleTodoCompleted",
    "AppendTodoList",
    "MessagesAppendTodoList",
    "ToggleSuggestedPostApproval",
    "MessagesToggleSuggestedPostApproval",
    "GetForumTopics",
    "MessagesGetForumTopics",
    "GetForumTopicsByID",
    "MessagesGetForumTopicsByID",
    "EditForumTopic",
    "MessagesEditForumTopic",
    "UpdatePinnedForumTopic",
    "MessagesUpdatePinnedForumTopic",
    "ReorderPinnedForumTopics",
    "MessagesReorderPinnedForumTopics",
    "CreateForumTopic",
    "MessagesCreateForumTopic",
    "DeleteTopicHistory",
    "MessagesDeleteTopicHistory",
    "GetEmojiGameInfo",
    "MessagesGetEmojiGameInfo",
    "SummarizeText",
    "MessagesSummarizeText",
    "EditChatCreator",
    "MessagesEditChatCreator",
    "GetFutureChatCreatorAfterLeave",
    "MessagesGetFutureChatCreatorAfterLeave",
    "EditChatParticipantRank",
    "MessagesEditChatParticipantRank",
    "DeclineUrlAuth",
    "MessagesDeclineUrlAuth",
    "CheckUrlAuthMatchCode",
    "MessagesCheckUrlAuthMatchCode",
    "ComposeMessageWithAI",
    "MessagesComposeMessageWithAI",
    "ReportReadMetrics",
    "MessagesReportReadMetrics",
    "ReportMusicListen",
    "MessagesReportMusicListen",
    "AddPollAnswer",
    "MessagesAddPollAnswer",
    "DeletePollAnswer",
    "MessagesDeletePollAnswer",
    "GetUnreadPollVotes",
    "MessagesGetUnreadPollVotes",
    "ReadPollVotes",
    "MessagesReadPollVotes",
    "SetBotGuestChatResult",
    "MessagesSetBotGuestChatResult",
    "DeleteParticipantReactions",
    "MessagesDeleteParticipantReactions",
    "DeleteParticipantReaction",
    "MessagesDeleteParticipantReaction",
    "GetPersonalChannelHistory",
    "MessagesGetPersonalChannelHistory"
]
