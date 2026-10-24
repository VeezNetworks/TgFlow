from ...tl import functions as _fn


GetCallConfig = getattr(_fn, 'GetCallConfig', getattr(_fn, 'PhoneGetCallConfig', None))
PhoneGetCallConfig = getattr(_fn, 'PhoneGetCallConfig', None)
RequestCall = getattr(_fn, 'RequestCall', getattr(_fn, 'PhoneRequestCall', None))
PhoneRequestCall = getattr(_fn, 'PhoneRequestCall', None)
AcceptCall = getattr(_fn, 'AcceptCall', getattr(_fn, 'PhoneAcceptCall', None))
PhoneAcceptCall = getattr(_fn, 'PhoneAcceptCall', None)
ConfirmCall = getattr(_fn, 'ConfirmCall', getattr(_fn, 'PhoneConfirmCall', None))
PhoneConfirmCall = getattr(_fn, 'PhoneConfirmCall', None)
ReceivedCall = getattr(_fn, 'ReceivedCall', getattr(_fn, 'PhoneReceivedCall', None))
PhoneReceivedCall = getattr(_fn, 'PhoneReceivedCall', None)
DiscardCall = getattr(_fn, 'DiscardCall', getattr(_fn, 'PhoneDiscardCall', None))
PhoneDiscardCall = getattr(_fn, 'PhoneDiscardCall', None)
SetCallRating = getattr(_fn, 'SetCallRating', getattr(_fn, 'PhoneSetCallRating', None))
PhoneSetCallRating = getattr(_fn, 'PhoneSetCallRating', None)
SaveCallDebug = getattr(_fn, 'SaveCallDebug', getattr(_fn, 'PhoneSaveCallDebug', None))
PhoneSaveCallDebug = getattr(_fn, 'PhoneSaveCallDebug', None)
SendSignalingData = getattr(_fn, 'SendSignalingData', getattr(_fn, 'PhoneSendSignalingData', None))
PhoneSendSignalingData = getattr(_fn, 'PhoneSendSignalingData', None)
CreateGroupCall = getattr(_fn, 'CreateGroupCall', getattr(_fn, 'PhoneCreateGroupCall', None))
PhoneCreateGroupCall = getattr(_fn, 'PhoneCreateGroupCall', None)
JoinGroupCall = getattr(_fn, 'JoinGroupCall', getattr(_fn, 'PhoneJoinGroupCall', None))
PhoneJoinGroupCall = getattr(_fn, 'PhoneJoinGroupCall', None)
LeaveGroupCall = getattr(_fn, 'LeaveGroupCall', getattr(_fn, 'PhoneLeaveGroupCall', None))
PhoneLeaveGroupCall = getattr(_fn, 'PhoneLeaveGroupCall', None)
InviteToGroupCall = getattr(_fn, 'InviteToGroupCall', getattr(_fn, 'PhoneInviteToGroupCall', None))
PhoneInviteToGroupCall = getattr(_fn, 'PhoneInviteToGroupCall', None)
DiscardGroupCall = getattr(_fn, 'DiscardGroupCall', getattr(_fn, 'PhoneDiscardGroupCall', None))
PhoneDiscardGroupCall = getattr(_fn, 'PhoneDiscardGroupCall', None)
ToggleGroupCallSettings = getattr(_fn, 'ToggleGroupCallSettings', getattr(_fn, 'PhoneToggleGroupCallSettings', None))
PhoneToggleGroupCallSettings = getattr(_fn, 'PhoneToggleGroupCallSettings', None)
GetGroupCall = getattr(_fn, 'GetGroupCall', getattr(_fn, 'PhoneGetGroupCall', None))
PhoneGetGroupCall = getattr(_fn, 'PhoneGetGroupCall', None)
GetGroupParticipants = getattr(_fn, 'GetGroupParticipants', getattr(_fn, 'PhoneGetGroupParticipants', None))
PhoneGetGroupParticipants = getattr(_fn, 'PhoneGetGroupParticipants', None)
CheckGroupCall = getattr(_fn, 'CheckGroupCall', getattr(_fn, 'PhoneCheckGroupCall', None))
PhoneCheckGroupCall = getattr(_fn, 'PhoneCheckGroupCall', None)
ToggleGroupCallRecord = getattr(_fn, 'ToggleGroupCallRecord', getattr(_fn, 'PhoneToggleGroupCallRecord', None))
PhoneToggleGroupCallRecord = getattr(_fn, 'PhoneToggleGroupCallRecord', None)
EditGroupCallParticipant = getattr(_fn, 'EditGroupCallParticipant', getattr(_fn, 'PhoneEditGroupCallParticipant', None))
PhoneEditGroupCallParticipant = getattr(_fn, 'PhoneEditGroupCallParticipant', None)
EditGroupCallTitle = getattr(_fn, 'EditGroupCallTitle', getattr(_fn, 'PhoneEditGroupCallTitle', None))
PhoneEditGroupCallTitle = getattr(_fn, 'PhoneEditGroupCallTitle', None)
GetGroupCallJoinAs = getattr(_fn, 'GetGroupCallJoinAs', getattr(_fn, 'PhoneGetGroupCallJoinAs', None))
PhoneGetGroupCallJoinAs = getattr(_fn, 'PhoneGetGroupCallJoinAs', None)
ExportGroupCallInvite = getattr(_fn, 'ExportGroupCallInvite', getattr(_fn, 'PhoneExportGroupCallInvite', None))
PhoneExportGroupCallInvite = getattr(_fn, 'PhoneExportGroupCallInvite', None)
ToggleGroupCallStartSubscription = getattr(_fn, 'ToggleGroupCallStartSubscription', getattr(_fn, 'PhoneToggleGroupCallStartSubscription', None))
PhoneToggleGroupCallStartSubscription = getattr(_fn, 'PhoneToggleGroupCallStartSubscription', None)
StartScheduledGroupCall = getattr(_fn, 'StartScheduledGroupCall', getattr(_fn, 'PhoneStartScheduledGroupCall', None))
PhoneStartScheduledGroupCall = getattr(_fn, 'PhoneStartScheduledGroupCall', None)
SaveDefaultGroupCallJoinAs = getattr(_fn, 'SaveDefaultGroupCallJoinAs', getattr(_fn, 'PhoneSaveDefaultGroupCallJoinAs', None))
PhoneSaveDefaultGroupCallJoinAs = getattr(_fn, 'PhoneSaveDefaultGroupCallJoinAs', None)
JoinGroupCallPresentation = getattr(_fn, 'JoinGroupCallPresentation', getattr(_fn, 'PhoneJoinGroupCallPresentation', None))
PhoneJoinGroupCallPresentation = getattr(_fn, 'PhoneJoinGroupCallPresentation', None)
LeaveGroupCallPresentation = getattr(_fn, 'LeaveGroupCallPresentation', getattr(_fn, 'PhoneLeaveGroupCallPresentation', None))
PhoneLeaveGroupCallPresentation = getattr(_fn, 'PhoneLeaveGroupCallPresentation', None)
GetGroupCallStreamChannels = getattr(_fn, 'GetGroupCallStreamChannels', getattr(_fn, 'PhoneGetGroupCallStreamChannels', None))
PhoneGetGroupCallStreamChannels = getattr(_fn, 'PhoneGetGroupCallStreamChannels', None)
GetGroupCallStreamRtmpUrl = getattr(_fn, 'GetGroupCallStreamRtmpUrl', getattr(_fn, 'PhoneGetGroupCallStreamRtmpUrl', None))
PhoneGetGroupCallStreamRtmpUrl = getattr(_fn, 'PhoneGetGroupCallStreamRtmpUrl', None)
SaveCallLog = getattr(_fn, 'SaveCallLog', getattr(_fn, 'PhoneSaveCallLog', None))
PhoneSaveCallLog = getattr(_fn, 'PhoneSaveCallLog', None)
CreateConferenceCall = getattr(_fn, 'CreateConferenceCall', getattr(_fn, 'PhoneCreateConferenceCall', None))
PhoneCreateConferenceCall = getattr(_fn, 'PhoneCreateConferenceCall', None)
DeleteConferenceCallParticipants = getattr(_fn, 'DeleteConferenceCallParticipants', getattr(_fn, 'PhoneDeleteConferenceCallParticipants', None))
PhoneDeleteConferenceCallParticipants = getattr(_fn, 'PhoneDeleteConferenceCallParticipants', None)
SendConferenceCallBroadcast = getattr(_fn, 'SendConferenceCallBroadcast', getattr(_fn, 'PhoneSendConferenceCallBroadcast', None))
PhoneSendConferenceCallBroadcast = getattr(_fn, 'PhoneSendConferenceCallBroadcast', None)
InviteConferenceCallParticipant = getattr(_fn, 'InviteConferenceCallParticipant', getattr(_fn, 'PhoneInviteConferenceCallParticipant', None))
PhoneInviteConferenceCallParticipant = getattr(_fn, 'PhoneInviteConferenceCallParticipant', None)
DeclineConferenceCallInvite = getattr(_fn, 'DeclineConferenceCallInvite', getattr(_fn, 'PhoneDeclineConferenceCallInvite', None))
PhoneDeclineConferenceCallInvite = getattr(_fn, 'PhoneDeclineConferenceCallInvite', None)
GetGroupCallChainBlocks = getattr(_fn, 'GetGroupCallChainBlocks', getattr(_fn, 'PhoneGetGroupCallChainBlocks', None))
PhoneGetGroupCallChainBlocks = getattr(_fn, 'PhoneGetGroupCallChainBlocks', None)
SendGroupCallMessage = getattr(_fn, 'SendGroupCallMessage', getattr(_fn, 'PhoneSendGroupCallMessage', None))
PhoneSendGroupCallMessage = getattr(_fn, 'PhoneSendGroupCallMessage', None)
SendGroupCallEncryptedMessage = getattr(_fn, 'SendGroupCallEncryptedMessage', getattr(_fn, 'PhoneSendGroupCallEncryptedMessage', None))
PhoneSendGroupCallEncryptedMessage = getattr(_fn, 'PhoneSendGroupCallEncryptedMessage', None)
DeleteGroupCallMessages = getattr(_fn, 'DeleteGroupCallMessages', getattr(_fn, 'PhoneDeleteGroupCallMessages', None))
PhoneDeleteGroupCallMessages = getattr(_fn, 'PhoneDeleteGroupCallMessages', None)
DeleteGroupCallParticipantMessages = getattr(_fn, 'DeleteGroupCallParticipantMessages', getattr(_fn, 'PhoneDeleteGroupCallParticipantMessages', None))
PhoneDeleteGroupCallParticipantMessages = getattr(_fn, 'PhoneDeleteGroupCallParticipantMessages', None)
GetGroupCallStars = getattr(_fn, 'GetGroupCallStars', getattr(_fn, 'PhoneGetGroupCallStars', None))
PhoneGetGroupCallStars = getattr(_fn, 'PhoneGetGroupCallStars', None)
SaveDefaultSendAs = getattr(_fn, 'SaveDefaultSendAs', getattr(_fn, 'PhoneSaveDefaultSendAs', None))
PhoneSaveDefaultSendAs = getattr(_fn, 'PhoneSaveDefaultSendAs', None)

__all__ = [
    "GetCallConfig",
    "PhoneGetCallConfig",
    "RequestCall",
    "PhoneRequestCall",
    "AcceptCall",
    "PhoneAcceptCall",
    "ConfirmCall",
    "PhoneConfirmCall",
    "ReceivedCall",
    "PhoneReceivedCall",
    "DiscardCall",
    "PhoneDiscardCall",
    "SetCallRating",
    "PhoneSetCallRating",
    "SaveCallDebug",
    "PhoneSaveCallDebug",
    "SendSignalingData",
    "PhoneSendSignalingData",
    "CreateGroupCall",
    "PhoneCreateGroupCall",
    "JoinGroupCall",
    "PhoneJoinGroupCall",
    "LeaveGroupCall",
    "PhoneLeaveGroupCall",
    "InviteToGroupCall",
    "PhoneInviteToGroupCall",
    "DiscardGroupCall",
    "PhoneDiscardGroupCall",
    "ToggleGroupCallSettings",
    "PhoneToggleGroupCallSettings",
    "GetGroupCall",
    "PhoneGetGroupCall",
    "GetGroupParticipants",
    "PhoneGetGroupParticipants",
    "CheckGroupCall",
    "PhoneCheckGroupCall",
    "ToggleGroupCallRecord",
    "PhoneToggleGroupCallRecord",
    "EditGroupCallParticipant",
    "PhoneEditGroupCallParticipant",
    "EditGroupCallTitle",
    "PhoneEditGroupCallTitle",
    "GetGroupCallJoinAs",
    "PhoneGetGroupCallJoinAs",
    "ExportGroupCallInvite",
    "PhoneExportGroupCallInvite",
    "ToggleGroupCallStartSubscription",
    "PhoneToggleGroupCallStartSubscription",
    "StartScheduledGroupCall",
    "PhoneStartScheduledGroupCall",
    "SaveDefaultGroupCallJoinAs",
    "PhoneSaveDefaultGroupCallJoinAs",
    "JoinGroupCallPresentation",
    "PhoneJoinGroupCallPresentation",
    "LeaveGroupCallPresentation",
    "PhoneLeaveGroupCallPresentation",
    "GetGroupCallStreamChannels",
    "PhoneGetGroupCallStreamChannels",
    "GetGroupCallStreamRtmpUrl",
    "PhoneGetGroupCallStreamRtmpUrl",
    "SaveCallLog",
    "PhoneSaveCallLog",
    "CreateConferenceCall",
    "PhoneCreateConferenceCall",
    "DeleteConferenceCallParticipants",
    "PhoneDeleteConferenceCallParticipants",
    "SendConferenceCallBroadcast",
    "PhoneSendConferenceCallBroadcast",
    "InviteConferenceCallParticipant",
    "PhoneInviteConferenceCallParticipant",
    "DeclineConferenceCallInvite",
    "PhoneDeclineConferenceCallInvite",
    "GetGroupCallChainBlocks",
    "PhoneGetGroupCallChainBlocks",
    "SendGroupCallMessage",
    "PhoneSendGroupCallMessage",
    "SendGroupCallEncryptedMessage",
    "PhoneSendGroupCallEncryptedMessage",
    "DeleteGroupCallMessages",
    "PhoneDeleteGroupCallMessages",
    "DeleteGroupCallParticipantMessages",
    "PhoneDeleteGroupCallParticipantMessages",
    "GetGroupCallStars",
    "PhoneGetGroupCallStars",
    "SaveDefaultSendAs",
    "PhoneSaveDefaultSendAs"
]
