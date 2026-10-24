from ...tl import functions as _fn


ReadHistory = getattr(_fn, 'ReadHistory', getattr(_fn, 'ChannelsReadHistory', None))
ChannelsReadHistory = getattr(_fn, 'ChannelsReadHistory', None)
DeleteMessages = getattr(_fn, 'DeleteMessages', getattr(_fn, 'ChannelsDeleteMessages', None))
ChannelsDeleteMessages = getattr(_fn, 'ChannelsDeleteMessages', None)
ReportSpam = getattr(_fn, 'ReportSpam', getattr(_fn, 'ChannelsReportSpam', None))
ChannelsReportSpam = getattr(_fn, 'ChannelsReportSpam', None)
GetMessages = getattr(_fn, 'GetMessages', getattr(_fn, 'ChannelsGetMessages', None))
ChannelsGetMessages = getattr(_fn, 'ChannelsGetMessages', None)
GetParticipants = getattr(_fn, 'GetParticipants', getattr(_fn, 'ChannelsGetParticipants', None))
ChannelsGetParticipants = getattr(_fn, 'ChannelsGetParticipants', None)
GetParticipant = getattr(_fn, 'GetParticipant', getattr(_fn, 'ChannelsGetParticipant', None))
ChannelsGetParticipant = getattr(_fn, 'ChannelsGetParticipant', None)
GetChannels = getattr(_fn, 'GetChannels', getattr(_fn, 'ChannelsGetChannels', None))
ChannelsGetChannels = getattr(_fn, 'ChannelsGetChannels', None)
GetFullChannel = getattr(_fn, 'GetFullChannel', getattr(_fn, 'ChannelsGetFullChannel', None))
ChannelsGetFullChannel = getattr(_fn, 'ChannelsGetFullChannel', None)
CreateChannel = getattr(_fn, 'CreateChannel', getattr(_fn, 'ChannelsCreateChannel', None))
ChannelsCreateChannel = getattr(_fn, 'ChannelsCreateChannel', None)
EditAdmin = getattr(_fn, 'EditAdmin', getattr(_fn, 'ChannelsEditAdmin', None))
ChannelsEditAdmin = getattr(_fn, 'ChannelsEditAdmin', None)
EditTitle = getattr(_fn, 'EditTitle', getattr(_fn, 'ChannelsEditTitle', None))
ChannelsEditTitle = getattr(_fn, 'ChannelsEditTitle', None)
EditPhoto = getattr(_fn, 'EditPhoto', getattr(_fn, 'ChannelsEditPhoto', None))
ChannelsEditPhoto = getattr(_fn, 'ChannelsEditPhoto', None)
CheckUsername = getattr(_fn, 'CheckUsername', getattr(_fn, 'ChannelsCheckUsername', None))
ChannelsCheckUsername = getattr(_fn, 'ChannelsCheckUsername', None)
UpdateUsername = getattr(_fn, 'UpdateUsername', getattr(_fn, 'ChannelsUpdateUsername', None))
ChannelsUpdateUsername = getattr(_fn, 'ChannelsUpdateUsername', None)
JoinChannel = getattr(_fn, 'JoinChannel', getattr(_fn, 'ChannelsJoinChannel', None))
ChannelsJoinChannel = getattr(_fn, 'ChannelsJoinChannel', None)
LeaveChannel = getattr(_fn, 'LeaveChannel', getattr(_fn, 'ChannelsLeaveChannel', None))
ChannelsLeaveChannel = getattr(_fn, 'ChannelsLeaveChannel', None)
InviteToChannel = getattr(_fn, 'InviteToChannel', getattr(_fn, 'ChannelsInviteToChannel', None))
ChannelsInviteToChannel = getattr(_fn, 'ChannelsInviteToChannel', None)
DeleteChannel = getattr(_fn, 'DeleteChannel', getattr(_fn, 'ChannelsDeleteChannel', None))
ChannelsDeleteChannel = getattr(_fn, 'ChannelsDeleteChannel', None)
ExportMessageLink = getattr(_fn, 'ExportMessageLink', getattr(_fn, 'ChannelsExportMessageLink', None))
ChannelsExportMessageLink = getattr(_fn, 'ChannelsExportMessageLink', None)
ToggleSignatures = getattr(_fn, 'ToggleSignatures', getattr(_fn, 'ChannelsToggleSignatures', None))
ChannelsToggleSignatures = getattr(_fn, 'ChannelsToggleSignatures', None)
GetAdminedPublicChannels = getattr(_fn, 'GetAdminedPublicChannels', getattr(_fn, 'ChannelsGetAdminedPublicChannels', None))
ChannelsGetAdminedPublicChannels = getattr(_fn, 'ChannelsGetAdminedPublicChannels', None)
EditBanned = getattr(_fn, 'EditBanned', getattr(_fn, 'ChannelsEditBanned', None))
ChannelsEditBanned = getattr(_fn, 'ChannelsEditBanned', None)
GetAdminLog = getattr(_fn, 'GetAdminLog', getattr(_fn, 'ChannelsGetAdminLog', None))
ChannelsGetAdminLog = getattr(_fn, 'ChannelsGetAdminLog', None)
SetStickers = getattr(_fn, 'SetStickers', getattr(_fn, 'ChannelsSetStickers', None))
ChannelsSetStickers = getattr(_fn, 'ChannelsSetStickers', None)
ReadMessageContents = getattr(_fn, 'ReadMessageContents', getattr(_fn, 'ChannelsReadMessageContents', None))
ChannelsReadMessageContents = getattr(_fn, 'ChannelsReadMessageContents', None)
DeleteHistory = getattr(_fn, 'DeleteHistory', getattr(_fn, 'ChannelsDeleteHistory', None))
ChannelsDeleteHistory = getattr(_fn, 'ChannelsDeleteHistory', None)
TogglePreHistoryHidden = getattr(_fn, 'TogglePreHistoryHidden', getattr(_fn, 'ChannelsTogglePreHistoryHidden', None))
ChannelsTogglePreHistoryHidden = getattr(_fn, 'ChannelsTogglePreHistoryHidden', None)
GetLeftChannels = getattr(_fn, 'GetLeftChannels', getattr(_fn, 'ChannelsGetLeftChannels', None))
ChannelsGetLeftChannels = getattr(_fn, 'ChannelsGetLeftChannels', None)
GetGroupsForDiscussion = getattr(_fn, 'GetGroupsForDiscussion', getattr(_fn, 'ChannelsGetGroupsForDiscussion', None))
ChannelsGetGroupsForDiscussion = getattr(_fn, 'ChannelsGetGroupsForDiscussion', None)
SetDiscussionGroup = getattr(_fn, 'SetDiscussionGroup', getattr(_fn, 'ChannelsSetDiscussionGroup', None))
ChannelsSetDiscussionGroup = getattr(_fn, 'ChannelsSetDiscussionGroup', None)
EditLocation = getattr(_fn, 'EditLocation', getattr(_fn, 'ChannelsEditLocation', None))
ChannelsEditLocation = getattr(_fn, 'ChannelsEditLocation', None)
ToggleSlowMode = getattr(_fn, 'ToggleSlowMode', getattr(_fn, 'ChannelsToggleSlowMode', None))
ChannelsToggleSlowMode = getattr(_fn, 'ChannelsToggleSlowMode', None)
GetInactiveChannels = getattr(_fn, 'GetInactiveChannels', getattr(_fn, 'ChannelsGetInactiveChannels', None))
ChannelsGetInactiveChannels = getattr(_fn, 'ChannelsGetInactiveChannels', None)
ConvertToGigagroup = getattr(_fn, 'ConvertToGigagroup', getattr(_fn, 'ChannelsConvertToGigagroup', None))
ChannelsConvertToGigagroup = getattr(_fn, 'ChannelsConvertToGigagroup', None)
GetSendAs = getattr(_fn, 'GetSendAs', getattr(_fn, 'ChannelsGetSendAs', None))
ChannelsGetSendAs = getattr(_fn, 'ChannelsGetSendAs', None)
DeleteParticipantHistory = getattr(_fn, 'DeleteParticipantHistory', getattr(_fn, 'ChannelsDeleteParticipantHistory', None))
ChannelsDeleteParticipantHistory = getattr(_fn, 'ChannelsDeleteParticipantHistory', None)
ToggleJoinToSend = getattr(_fn, 'ToggleJoinToSend', getattr(_fn, 'ChannelsToggleJoinToSend', None))
ChannelsToggleJoinToSend = getattr(_fn, 'ChannelsToggleJoinToSend', None)
ToggleJoinRequest = getattr(_fn, 'ToggleJoinRequest', getattr(_fn, 'ChannelsToggleJoinRequest', None))
ChannelsToggleJoinRequest = getattr(_fn, 'ChannelsToggleJoinRequest', None)
ReorderUsernames = getattr(_fn, 'ReorderUsernames', getattr(_fn, 'ChannelsReorderUsernames', None))
ChannelsReorderUsernames = getattr(_fn, 'ChannelsReorderUsernames', None)
ToggleUsername = getattr(_fn, 'ToggleUsername', getattr(_fn, 'ChannelsToggleUsername', None))
ChannelsToggleUsername = getattr(_fn, 'ChannelsToggleUsername', None)
DeactivateAllUsernames = getattr(_fn, 'DeactivateAllUsernames', getattr(_fn, 'ChannelsDeactivateAllUsernames', None))
ChannelsDeactivateAllUsernames = getattr(_fn, 'ChannelsDeactivateAllUsernames', None)
ToggleForum = getattr(_fn, 'ToggleForum', getattr(_fn, 'ChannelsToggleForum', None))
ChannelsToggleForum = getattr(_fn, 'ChannelsToggleForum', None)
ToggleAntiSpam = getattr(_fn, 'ToggleAntiSpam', getattr(_fn, 'ChannelsToggleAntiSpam', None))
ChannelsToggleAntiSpam = getattr(_fn, 'ChannelsToggleAntiSpam', None)
ReportAntiSpamFalsePositive = getattr(_fn, 'ReportAntiSpamFalsePositive', getattr(_fn, 'ChannelsReportAntiSpamFalsePositive', None))
ChannelsReportAntiSpamFalsePositive = getattr(_fn, 'ChannelsReportAntiSpamFalsePositive', None)
ToggleParticipantsHidden = getattr(_fn, 'ToggleParticipantsHidden', getattr(_fn, 'ChannelsToggleParticipantsHidden', None))
ChannelsToggleParticipantsHidden = getattr(_fn, 'ChannelsToggleParticipantsHidden', None)
UpdateColor = getattr(_fn, 'UpdateColor', getattr(_fn, 'ChannelsUpdateColor', None))
ChannelsUpdateColor = getattr(_fn, 'ChannelsUpdateColor', None)
ToggleViewForumAsMessages = getattr(_fn, 'ToggleViewForumAsMessages', getattr(_fn, 'ChannelsToggleViewForumAsMessages', None))
ChannelsToggleViewForumAsMessages = getattr(_fn, 'ChannelsToggleViewForumAsMessages', None)
GetChannelRecommendations = getattr(_fn, 'GetChannelRecommendations', getattr(_fn, 'ChannelsGetChannelRecommendations', None))
ChannelsGetChannelRecommendations = getattr(_fn, 'ChannelsGetChannelRecommendations', None)
UpdateEmojiStatus = getattr(_fn, 'UpdateEmojiStatus', getattr(_fn, 'ChannelsUpdateEmojiStatus', None))
ChannelsUpdateEmojiStatus = getattr(_fn, 'ChannelsUpdateEmojiStatus', None)
SetBoostsToUnblockRestrictions = getattr(_fn, 'SetBoostsToUnblockRestrictions', getattr(_fn, 'ChannelsSetBoostsToUnblockRestrictions', None))
ChannelsSetBoostsToUnblockRestrictions = getattr(_fn, 'ChannelsSetBoostsToUnblockRestrictions', None)
SetEmojiStickers = getattr(_fn, 'SetEmojiStickers', getattr(_fn, 'ChannelsSetEmojiStickers', None))
ChannelsSetEmojiStickers = getattr(_fn, 'ChannelsSetEmojiStickers', None)
RestrictSponsoredMessages = getattr(_fn, 'RestrictSponsoredMessages', getattr(_fn, 'ChannelsRestrictSponsoredMessages', None))
ChannelsRestrictSponsoredMessages = getattr(_fn, 'ChannelsRestrictSponsoredMessages', None)
SearchPosts = getattr(_fn, 'SearchPosts', getattr(_fn, 'ChannelsSearchPosts', None))
ChannelsSearchPosts = getattr(_fn, 'ChannelsSearchPosts', None)
UpdatePaidMessagesPrice = getattr(_fn, 'UpdatePaidMessagesPrice', getattr(_fn, 'ChannelsUpdatePaidMessagesPrice', None))
ChannelsUpdatePaidMessagesPrice = getattr(_fn, 'ChannelsUpdatePaidMessagesPrice', None)
ToggleAutotranslation = getattr(_fn, 'ToggleAutotranslation', getattr(_fn, 'ChannelsToggleAutotranslation', None))
ChannelsToggleAutotranslation = getattr(_fn, 'ChannelsToggleAutotranslation', None)
GetMessageAuthor = getattr(_fn, 'GetMessageAuthor', getattr(_fn, 'ChannelsGetMessageAuthor', None))
ChannelsGetMessageAuthor = getattr(_fn, 'ChannelsGetMessageAuthor', None)
CheckSearchPostsFlood = getattr(_fn, 'CheckSearchPostsFlood', getattr(_fn, 'ChannelsCheckSearchPostsFlood', None))
ChannelsCheckSearchPostsFlood = getattr(_fn, 'ChannelsCheckSearchPostsFlood', None)
SetMainProfileTab = getattr(_fn, 'SetMainProfileTab', getattr(_fn, 'ChannelsSetMainProfileTab', None))
ChannelsSetMainProfileTab = getattr(_fn, 'ChannelsSetMainProfileTab', None)

__all__ = [
    "ReadHistory",
    "ChannelsReadHistory",
    "DeleteMessages",
    "ChannelsDeleteMessages",
    "ReportSpam",
    "ChannelsReportSpam",
    "GetMessages",
    "ChannelsGetMessages",
    "GetParticipants",
    "ChannelsGetParticipants",
    "GetParticipant",
    "ChannelsGetParticipant",
    "GetChannels",
    "ChannelsGetChannels",
    "GetFullChannel",
    "ChannelsGetFullChannel",
    "CreateChannel",
    "ChannelsCreateChannel",
    "EditAdmin",
    "ChannelsEditAdmin",
    "EditTitle",
    "ChannelsEditTitle",
    "EditPhoto",
    "ChannelsEditPhoto",
    "CheckUsername",
    "ChannelsCheckUsername",
    "UpdateUsername",
    "ChannelsUpdateUsername",
    "JoinChannel",
    "ChannelsJoinChannel",
    "LeaveChannel",
    "ChannelsLeaveChannel",
    "InviteToChannel",
    "ChannelsInviteToChannel",
    "DeleteChannel",
    "ChannelsDeleteChannel",
    "ExportMessageLink",
    "ChannelsExportMessageLink",
    "ToggleSignatures",
    "ChannelsToggleSignatures",
    "GetAdminedPublicChannels",
    "ChannelsGetAdminedPublicChannels",
    "EditBanned",
    "ChannelsEditBanned",
    "GetAdminLog",
    "ChannelsGetAdminLog",
    "SetStickers",
    "ChannelsSetStickers",
    "ReadMessageContents",
    "ChannelsReadMessageContents",
    "DeleteHistory",
    "ChannelsDeleteHistory",
    "TogglePreHistoryHidden",
    "ChannelsTogglePreHistoryHidden",
    "GetLeftChannels",
    "ChannelsGetLeftChannels",
    "GetGroupsForDiscussion",
    "ChannelsGetGroupsForDiscussion",
    "SetDiscussionGroup",
    "ChannelsSetDiscussionGroup",
    "EditLocation",
    "ChannelsEditLocation",
    "ToggleSlowMode",
    "ChannelsToggleSlowMode",
    "GetInactiveChannels",
    "ChannelsGetInactiveChannels",
    "ConvertToGigagroup",
    "ChannelsConvertToGigagroup",
    "GetSendAs",
    "ChannelsGetSendAs",
    "DeleteParticipantHistory",
    "ChannelsDeleteParticipantHistory",
    "ToggleJoinToSend",
    "ChannelsToggleJoinToSend",
    "ToggleJoinRequest",
    "ChannelsToggleJoinRequest",
    "ReorderUsernames",
    "ChannelsReorderUsernames",
    "ToggleUsername",
    "ChannelsToggleUsername",
    "DeactivateAllUsernames",
    "ChannelsDeactivateAllUsernames",
    "ToggleForum",
    "ChannelsToggleForum",
    "ToggleAntiSpam",
    "ChannelsToggleAntiSpam",
    "ReportAntiSpamFalsePositive",
    "ChannelsReportAntiSpamFalsePositive",
    "ToggleParticipantsHidden",
    "ChannelsToggleParticipantsHidden",
    "UpdateColor",
    "ChannelsUpdateColor",
    "ToggleViewForumAsMessages",
    "ChannelsToggleViewForumAsMessages",
    "GetChannelRecommendations",
    "ChannelsGetChannelRecommendations",
    "UpdateEmojiStatus",
    "ChannelsUpdateEmojiStatus",
    "SetBoostsToUnblockRestrictions",
    "ChannelsSetBoostsToUnblockRestrictions",
    "SetEmojiStickers",
    "ChannelsSetEmojiStickers",
    "RestrictSponsoredMessages",
    "ChannelsRestrictSponsoredMessages",
    "SearchPosts",
    "ChannelsSearchPosts",
    "UpdatePaidMessagesPrice",
    "ChannelsUpdatePaidMessagesPrice",
    "ToggleAutotranslation",
    "ChannelsToggleAutotranslation",
    "GetMessageAuthor",
    "ChannelsGetMessageAuthor",
    "CheckSearchPostsFlood",
    "ChannelsCheckSearchPostsFlood",
    "SetMainProfileTab",
    "ChannelsSetMainProfileTab"
]
