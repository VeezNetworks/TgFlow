from ...tl import functions as _fn


RegisterDevice = getattr(_fn, 'RegisterDevice', getattr(_fn, 'AccountRegisterDevice', None))
AccountRegisterDevice = getattr(_fn, 'AccountRegisterDevice', None)
UnregisterDevice = getattr(_fn, 'UnregisterDevice', getattr(_fn, 'AccountUnregisterDevice', None))
AccountUnregisterDevice = getattr(_fn, 'AccountUnregisterDevice', None)
UpdateNotifySettings = getattr(_fn, 'UpdateNotifySettings', getattr(_fn, 'AccountUpdateNotifySettings', None))
AccountUpdateNotifySettings = getattr(_fn, 'AccountUpdateNotifySettings', None)
GetNotifySettings = getattr(_fn, 'GetNotifySettings', getattr(_fn, 'AccountGetNotifySettings', None))
AccountGetNotifySettings = getattr(_fn, 'AccountGetNotifySettings', None)
ResetNotifySettings = getattr(_fn, 'ResetNotifySettings', getattr(_fn, 'AccountResetNotifySettings', None))
AccountResetNotifySettings = getattr(_fn, 'AccountResetNotifySettings', None)
UpdateProfile = getattr(_fn, 'UpdateProfile', getattr(_fn, 'AccountUpdateProfile', None))
AccountUpdateProfile = getattr(_fn, 'AccountUpdateProfile', None)
UpdateStatus = getattr(_fn, 'UpdateStatus', getattr(_fn, 'AccountUpdateStatus', None))
AccountUpdateStatus = getattr(_fn, 'AccountUpdateStatus', None)
GetWallPapers = getattr(_fn, 'GetWallPapers', getattr(_fn, 'AccountGetWallPapers', None))
AccountGetWallPapers = getattr(_fn, 'AccountGetWallPapers', None)
ReportPeer = getattr(_fn, 'ReportPeer', getattr(_fn, 'AccountReportPeer', None))
AccountReportPeer = getattr(_fn, 'AccountReportPeer', None)
CheckUsername = getattr(_fn, 'CheckUsername', getattr(_fn, 'AccountCheckUsername', None))
AccountCheckUsername = getattr(_fn, 'AccountCheckUsername', None)
UpdateUsername = getattr(_fn, 'UpdateUsername', getattr(_fn, 'AccountUpdateUsername', None))
AccountUpdateUsername = getattr(_fn, 'AccountUpdateUsername', None)
GetPrivacy = getattr(_fn, 'GetPrivacy', getattr(_fn, 'AccountGetPrivacy', None))
AccountGetPrivacy = getattr(_fn, 'AccountGetPrivacy', None)
SetPrivacy = getattr(_fn, 'SetPrivacy', getattr(_fn, 'AccountSetPrivacy', None))
AccountSetPrivacy = getattr(_fn, 'AccountSetPrivacy', None)
DeleteAccount = getattr(_fn, 'DeleteAccount', getattr(_fn, 'AccountDeleteAccount', None))
AccountDeleteAccount = getattr(_fn, 'AccountDeleteAccount', None)
GetAccountTTL = getattr(_fn, 'GetAccountTTL', getattr(_fn, 'AccountGetAccountTTL', None))
AccountGetAccountTTL = getattr(_fn, 'AccountGetAccountTTL', None)
SetAccountTTL = getattr(_fn, 'SetAccountTTL', getattr(_fn, 'AccountSetAccountTTL', None))
AccountSetAccountTTL = getattr(_fn, 'AccountSetAccountTTL', None)
SendChangePhoneCode = getattr(_fn, 'SendChangePhoneCode', getattr(_fn, 'AccountSendChangePhoneCode', None))
AccountSendChangePhoneCode = getattr(_fn, 'AccountSendChangePhoneCode', None)
ChangePhone = getattr(_fn, 'ChangePhone', getattr(_fn, 'AccountChangePhone', None))
AccountChangePhone = getattr(_fn, 'AccountChangePhone', None)
UpdateDeviceLocked = getattr(_fn, 'UpdateDeviceLocked', getattr(_fn, 'AccountUpdateDeviceLocked', None))
AccountUpdateDeviceLocked = getattr(_fn, 'AccountUpdateDeviceLocked', None)
GetAuthorizations = getattr(_fn, 'GetAuthorizations', getattr(_fn, 'AccountGetAuthorizations', None))
AccountGetAuthorizations = getattr(_fn, 'AccountGetAuthorizations', None)
ResetAuthorization = getattr(_fn, 'ResetAuthorization', getattr(_fn, 'AccountResetAuthorization', None))
AccountResetAuthorization = getattr(_fn, 'AccountResetAuthorization', None)
GetPassword = getattr(_fn, 'GetPassword', getattr(_fn, 'AccountGetPassword', None))
AccountGetPassword = getattr(_fn, 'AccountGetPassword', None)
GetPasswordSettings = getattr(_fn, 'GetPasswordSettings', getattr(_fn, 'AccountGetPasswordSettings', None))
AccountGetPasswordSettings = getattr(_fn, 'AccountGetPasswordSettings', None)
UpdatePasswordSettings = getattr(_fn, 'UpdatePasswordSettings', getattr(_fn, 'AccountUpdatePasswordSettings', None))
AccountUpdatePasswordSettings = getattr(_fn, 'AccountUpdatePasswordSettings', None)
SendConfirmPhoneCode = getattr(_fn, 'SendConfirmPhoneCode', getattr(_fn, 'AccountSendConfirmPhoneCode', None))
AccountSendConfirmPhoneCode = getattr(_fn, 'AccountSendConfirmPhoneCode', None)
ConfirmPhone = getattr(_fn, 'ConfirmPhone', getattr(_fn, 'AccountConfirmPhone', None))
AccountConfirmPhone = getattr(_fn, 'AccountConfirmPhone', None)
GetTmpPassword = getattr(_fn, 'GetTmpPassword', getattr(_fn, 'AccountGetTmpPassword', None))
AccountGetTmpPassword = getattr(_fn, 'AccountGetTmpPassword', None)
GetWebAuthorizations = getattr(_fn, 'GetWebAuthorizations', getattr(_fn, 'AccountGetWebAuthorizations', None))
AccountGetWebAuthorizations = getattr(_fn, 'AccountGetWebAuthorizations', None)
ResetWebAuthorization = getattr(_fn, 'ResetWebAuthorization', getattr(_fn, 'AccountResetWebAuthorization', None))
AccountResetWebAuthorization = getattr(_fn, 'AccountResetWebAuthorization', None)
ResetWebAuthorizations = getattr(_fn, 'ResetWebAuthorizations', getattr(_fn, 'AccountResetWebAuthorizations', None))
AccountResetWebAuthorizations = getattr(_fn, 'AccountResetWebAuthorizations', None)
GetAllSecureValues = getattr(_fn, 'GetAllSecureValues', getattr(_fn, 'AccountGetAllSecureValues', None))
AccountGetAllSecureValues = getattr(_fn, 'AccountGetAllSecureValues', None)
GetSecureValue = getattr(_fn, 'GetSecureValue', getattr(_fn, 'AccountGetSecureValue', None))
AccountGetSecureValue = getattr(_fn, 'AccountGetSecureValue', None)
SaveSecureValue = getattr(_fn, 'SaveSecureValue', getattr(_fn, 'AccountSaveSecureValue', None))
AccountSaveSecureValue = getattr(_fn, 'AccountSaveSecureValue', None)
DeleteSecureValue = getattr(_fn, 'DeleteSecureValue', getattr(_fn, 'AccountDeleteSecureValue', None))
AccountDeleteSecureValue = getattr(_fn, 'AccountDeleteSecureValue', None)
GetAuthorizationForm = getattr(_fn, 'GetAuthorizationForm', getattr(_fn, 'AccountGetAuthorizationForm', None))
AccountGetAuthorizationForm = getattr(_fn, 'AccountGetAuthorizationForm', None)
AcceptAuthorization = getattr(_fn, 'AcceptAuthorization', getattr(_fn, 'AccountAcceptAuthorization', None))
AccountAcceptAuthorization = getattr(_fn, 'AccountAcceptAuthorization', None)
SendVerifyPhoneCode = getattr(_fn, 'SendVerifyPhoneCode', getattr(_fn, 'AccountSendVerifyPhoneCode', None))
AccountSendVerifyPhoneCode = getattr(_fn, 'AccountSendVerifyPhoneCode', None)
VerifyPhone = getattr(_fn, 'VerifyPhone', getattr(_fn, 'AccountVerifyPhone', None))
AccountVerifyPhone = getattr(_fn, 'AccountVerifyPhone', None)
SendVerifyEmailCode = getattr(_fn, 'SendVerifyEmailCode', getattr(_fn, 'AccountSendVerifyEmailCode', None))
AccountSendVerifyEmailCode = getattr(_fn, 'AccountSendVerifyEmailCode', None)
VerifyEmail = getattr(_fn, 'VerifyEmail', getattr(_fn, 'AccountVerifyEmail', None))
AccountVerifyEmail = getattr(_fn, 'AccountVerifyEmail', None)
InitTakeoutSession = getattr(_fn, 'InitTakeoutSession', getattr(_fn, 'AccountInitTakeoutSession', None))
AccountInitTakeoutSession = getattr(_fn, 'AccountInitTakeoutSession', None)
FinishTakeoutSession = getattr(_fn, 'FinishTakeoutSession', getattr(_fn, 'AccountFinishTakeoutSession', None))
AccountFinishTakeoutSession = getattr(_fn, 'AccountFinishTakeoutSession', None)
ConfirmPasswordEmail = getattr(_fn, 'ConfirmPasswordEmail', getattr(_fn, 'AccountConfirmPasswordEmail', None))
AccountConfirmPasswordEmail = getattr(_fn, 'AccountConfirmPasswordEmail', None)
ResendPasswordEmail = getattr(_fn, 'ResendPasswordEmail', getattr(_fn, 'AccountResendPasswordEmail', None))
AccountResendPasswordEmail = getattr(_fn, 'AccountResendPasswordEmail', None)
CancelPasswordEmail = getattr(_fn, 'CancelPasswordEmail', getattr(_fn, 'AccountCancelPasswordEmail', None))
AccountCancelPasswordEmail = getattr(_fn, 'AccountCancelPasswordEmail', None)
GetContactSignUpNotification = getattr(_fn, 'GetContactSignUpNotification', getattr(_fn, 'AccountGetContactSignUpNotification', None))
AccountGetContactSignUpNotification = getattr(_fn, 'AccountGetContactSignUpNotification', None)
SetContactSignUpNotification = getattr(_fn, 'SetContactSignUpNotification', getattr(_fn, 'AccountSetContactSignUpNotification', None))
AccountSetContactSignUpNotification = getattr(_fn, 'AccountSetContactSignUpNotification', None)
GetNotifyExceptions = getattr(_fn, 'GetNotifyExceptions', getattr(_fn, 'AccountGetNotifyExceptions', None))
AccountGetNotifyExceptions = getattr(_fn, 'AccountGetNotifyExceptions', None)
GetWallPaper = getattr(_fn, 'GetWallPaper', getattr(_fn, 'AccountGetWallPaper', None))
AccountGetWallPaper = getattr(_fn, 'AccountGetWallPaper', None)
UploadWallPaper = getattr(_fn, 'UploadWallPaper', getattr(_fn, 'AccountUploadWallPaper', None))
AccountUploadWallPaper = getattr(_fn, 'AccountUploadWallPaper', None)
SaveWallPaper = getattr(_fn, 'SaveWallPaper', getattr(_fn, 'AccountSaveWallPaper', None))
AccountSaveWallPaper = getattr(_fn, 'AccountSaveWallPaper', None)
InstallWallPaper = getattr(_fn, 'InstallWallPaper', getattr(_fn, 'AccountInstallWallPaper', None))
AccountInstallWallPaper = getattr(_fn, 'AccountInstallWallPaper', None)
ResetWallPapers = getattr(_fn, 'ResetWallPapers', getattr(_fn, 'AccountResetWallPapers', None))
AccountResetWallPapers = getattr(_fn, 'AccountResetWallPapers', None)
GetAutoDownloadSettings = getattr(_fn, 'GetAutoDownloadSettings', getattr(_fn, 'AccountGetAutoDownloadSettings', None))
AccountGetAutoDownloadSettings = getattr(_fn, 'AccountGetAutoDownloadSettings', None)
SaveAutoDownloadSettings = getattr(_fn, 'SaveAutoDownloadSettings', getattr(_fn, 'AccountSaveAutoDownloadSettings', None))
AccountSaveAutoDownloadSettings = getattr(_fn, 'AccountSaveAutoDownloadSettings', None)
UploadTheme = getattr(_fn, 'UploadTheme', getattr(_fn, 'AccountUploadTheme', None))
AccountUploadTheme = getattr(_fn, 'AccountUploadTheme', None)
CreateTheme = getattr(_fn, 'CreateTheme', getattr(_fn, 'AccountCreateTheme', None))
AccountCreateTheme = getattr(_fn, 'AccountCreateTheme', None)
UpdateTheme = getattr(_fn, 'UpdateTheme', getattr(_fn, 'AccountUpdateTheme', None))
AccountUpdateTheme = getattr(_fn, 'AccountUpdateTheme', None)
SaveTheme = getattr(_fn, 'SaveTheme', getattr(_fn, 'AccountSaveTheme', None))
AccountSaveTheme = getattr(_fn, 'AccountSaveTheme', None)
InstallTheme = getattr(_fn, 'InstallTheme', getattr(_fn, 'AccountInstallTheme', None))
AccountInstallTheme = getattr(_fn, 'AccountInstallTheme', None)
GetTheme = getattr(_fn, 'GetTheme', getattr(_fn, 'AccountGetTheme', None))
AccountGetTheme = getattr(_fn, 'AccountGetTheme', None)
GetThemes = getattr(_fn, 'GetThemes', getattr(_fn, 'AccountGetThemes', None))
AccountGetThemes = getattr(_fn, 'AccountGetThemes', None)
SetContentSettings = getattr(_fn, 'SetContentSettings', getattr(_fn, 'AccountSetContentSettings', None))
AccountSetContentSettings = getattr(_fn, 'AccountSetContentSettings', None)
GetContentSettings = getattr(_fn, 'GetContentSettings', getattr(_fn, 'AccountGetContentSettings', None))
AccountGetContentSettings = getattr(_fn, 'AccountGetContentSettings', None)
GetMultiWallPapers = getattr(_fn, 'GetMultiWallPapers', getattr(_fn, 'AccountGetMultiWallPapers', None))
AccountGetMultiWallPapers = getattr(_fn, 'AccountGetMultiWallPapers', None)
GetGlobalPrivacySettings = getattr(_fn, 'GetGlobalPrivacySettings', getattr(_fn, 'AccountGetGlobalPrivacySettings', None))
AccountGetGlobalPrivacySettings = getattr(_fn, 'AccountGetGlobalPrivacySettings', None)
SetGlobalPrivacySettings = getattr(_fn, 'SetGlobalPrivacySettings', getattr(_fn, 'AccountSetGlobalPrivacySettings', None))
AccountSetGlobalPrivacySettings = getattr(_fn, 'AccountSetGlobalPrivacySettings', None)
ReportProfilePhoto = getattr(_fn, 'ReportProfilePhoto', getattr(_fn, 'AccountReportProfilePhoto', None))
AccountReportProfilePhoto = getattr(_fn, 'AccountReportProfilePhoto', None)
ResetPassword = getattr(_fn, 'ResetPassword', getattr(_fn, 'AccountResetPassword', None))
AccountResetPassword = getattr(_fn, 'AccountResetPassword', None)
DeclinePasswordReset = getattr(_fn, 'DeclinePasswordReset', getattr(_fn, 'AccountDeclinePasswordReset', None))
AccountDeclinePasswordReset = getattr(_fn, 'AccountDeclinePasswordReset', None)
GetChatThemes = getattr(_fn, 'GetChatThemes', getattr(_fn, 'AccountGetChatThemes', None))
AccountGetChatThemes = getattr(_fn, 'AccountGetChatThemes', None)
SetAuthorizationTTL = getattr(_fn, 'SetAuthorizationTTL', getattr(_fn, 'AccountSetAuthorizationTTL', None))
AccountSetAuthorizationTTL = getattr(_fn, 'AccountSetAuthorizationTTL', None)
ChangeAuthorizationSettings = getattr(_fn, 'ChangeAuthorizationSettings', getattr(_fn, 'AccountChangeAuthorizationSettings', None))
AccountChangeAuthorizationSettings = getattr(_fn, 'AccountChangeAuthorizationSettings', None)
GetSavedRingtones = getattr(_fn, 'GetSavedRingtones', getattr(_fn, 'AccountGetSavedRingtones', None))
AccountGetSavedRingtones = getattr(_fn, 'AccountGetSavedRingtones', None)
SaveRingtone = getattr(_fn, 'SaveRingtone', getattr(_fn, 'AccountSaveRingtone', None))
AccountSaveRingtone = getattr(_fn, 'AccountSaveRingtone', None)
UploadRingtone = getattr(_fn, 'UploadRingtone', getattr(_fn, 'AccountUploadRingtone', None))
AccountUploadRingtone = getattr(_fn, 'AccountUploadRingtone', None)
UpdateEmojiStatus = getattr(_fn, 'UpdateEmojiStatus', getattr(_fn, 'AccountUpdateEmojiStatus', None))
AccountUpdateEmojiStatus = getattr(_fn, 'AccountUpdateEmojiStatus', None)
GetDefaultEmojiStatuses = getattr(_fn, 'GetDefaultEmojiStatuses', getattr(_fn, 'AccountGetDefaultEmojiStatuses', None))
AccountGetDefaultEmojiStatuses = getattr(_fn, 'AccountGetDefaultEmojiStatuses', None)
GetRecentEmojiStatuses = getattr(_fn, 'GetRecentEmojiStatuses', getattr(_fn, 'AccountGetRecentEmojiStatuses', None))
AccountGetRecentEmojiStatuses = getattr(_fn, 'AccountGetRecentEmojiStatuses', None)
ClearRecentEmojiStatuses = getattr(_fn, 'ClearRecentEmojiStatuses', getattr(_fn, 'AccountClearRecentEmojiStatuses', None))
AccountClearRecentEmojiStatuses = getattr(_fn, 'AccountClearRecentEmojiStatuses', None)
ReorderUsernames = getattr(_fn, 'ReorderUsernames', getattr(_fn, 'AccountReorderUsernames', None))
AccountReorderUsernames = getattr(_fn, 'AccountReorderUsernames', None)
ToggleUsername = getattr(_fn, 'ToggleUsername', getattr(_fn, 'AccountToggleUsername', None))
AccountToggleUsername = getattr(_fn, 'AccountToggleUsername', None)
GetDefaultProfilePhotoEmojis = getattr(_fn, 'GetDefaultProfilePhotoEmojis', getattr(_fn, 'AccountGetDefaultProfilePhotoEmojis', None))
AccountGetDefaultProfilePhotoEmojis = getattr(_fn, 'AccountGetDefaultProfilePhotoEmojis', None)
GetDefaultGroupPhotoEmojis = getattr(_fn, 'GetDefaultGroupPhotoEmojis', getattr(_fn, 'AccountGetDefaultGroupPhotoEmojis', None))
AccountGetDefaultGroupPhotoEmojis = getattr(_fn, 'AccountGetDefaultGroupPhotoEmojis', None)
GetAutoSaveSettings = getattr(_fn, 'GetAutoSaveSettings', getattr(_fn, 'AccountGetAutoSaveSettings', None))
AccountGetAutoSaveSettings = getattr(_fn, 'AccountGetAutoSaveSettings', None)
SaveAutoSaveSettings = getattr(_fn, 'SaveAutoSaveSettings', getattr(_fn, 'AccountSaveAutoSaveSettings', None))
AccountSaveAutoSaveSettings = getattr(_fn, 'AccountSaveAutoSaveSettings', None)
DeleteAutoSaveExceptions = getattr(_fn, 'DeleteAutoSaveExceptions', getattr(_fn, 'AccountDeleteAutoSaveExceptions', None))
AccountDeleteAutoSaveExceptions = getattr(_fn, 'AccountDeleteAutoSaveExceptions', None)
InvalidateSignInCodes = getattr(_fn, 'InvalidateSignInCodes', getattr(_fn, 'AccountInvalidateSignInCodes', None))
AccountInvalidateSignInCodes = getattr(_fn, 'AccountInvalidateSignInCodes', None)
UpdateColor = getattr(_fn, 'UpdateColor', getattr(_fn, 'AccountUpdateColor', None))
AccountUpdateColor = getattr(_fn, 'AccountUpdateColor', None)
GetDefaultBackgroundEmojis = getattr(_fn, 'GetDefaultBackgroundEmojis', getattr(_fn, 'AccountGetDefaultBackgroundEmojis', None))
AccountGetDefaultBackgroundEmojis = getattr(_fn, 'AccountGetDefaultBackgroundEmojis', None)
GetChannelDefaultEmojiStatuses = getattr(_fn, 'GetChannelDefaultEmojiStatuses', getattr(_fn, 'AccountGetChannelDefaultEmojiStatuses', None))
AccountGetChannelDefaultEmojiStatuses = getattr(_fn, 'AccountGetChannelDefaultEmojiStatuses', None)
GetChannelRestrictedStatusEmojis = getattr(_fn, 'GetChannelRestrictedStatusEmojis', getattr(_fn, 'AccountGetChannelRestrictedStatusEmojis', None))
AccountGetChannelRestrictedStatusEmojis = getattr(_fn, 'AccountGetChannelRestrictedStatusEmojis', None)
UpdateBusinessWorkHours = getattr(_fn, 'UpdateBusinessWorkHours', getattr(_fn, 'AccountUpdateBusinessWorkHours', None))
AccountUpdateBusinessWorkHours = getattr(_fn, 'AccountUpdateBusinessWorkHours', None)
UpdateBusinessLocation = getattr(_fn, 'UpdateBusinessLocation', getattr(_fn, 'AccountUpdateBusinessLocation', None))
AccountUpdateBusinessLocation = getattr(_fn, 'AccountUpdateBusinessLocation', None)
UpdateBusinessGreetingMessage = getattr(_fn, 'UpdateBusinessGreetingMessage', getattr(_fn, 'AccountUpdateBusinessGreetingMessage', None))
AccountUpdateBusinessGreetingMessage = getattr(_fn, 'AccountUpdateBusinessGreetingMessage', None)
UpdateBusinessAwayMessage = getattr(_fn, 'UpdateBusinessAwayMessage', getattr(_fn, 'AccountUpdateBusinessAwayMessage', None))
AccountUpdateBusinessAwayMessage = getattr(_fn, 'AccountUpdateBusinessAwayMessage', None)
UpdateConnectedBot = getattr(_fn, 'UpdateConnectedBot', getattr(_fn, 'AccountUpdateConnectedBot', None))
AccountUpdateConnectedBot = getattr(_fn, 'AccountUpdateConnectedBot', None)
GetConnectedBots = getattr(_fn, 'GetConnectedBots', getattr(_fn, 'AccountGetConnectedBots', None))
AccountGetConnectedBots = getattr(_fn, 'AccountGetConnectedBots', None)
GetBotBusinessConnection = getattr(_fn, 'GetBotBusinessConnection', getattr(_fn, 'AccountGetBotBusinessConnection', None))
AccountGetBotBusinessConnection = getattr(_fn, 'AccountGetBotBusinessConnection', None)
UpdateBusinessIntro = getattr(_fn, 'UpdateBusinessIntro', getattr(_fn, 'AccountUpdateBusinessIntro', None))
AccountUpdateBusinessIntro = getattr(_fn, 'AccountUpdateBusinessIntro', None)
ToggleConnectedBotPaused = getattr(_fn, 'ToggleConnectedBotPaused', getattr(_fn, 'AccountToggleConnectedBotPaused', None))
AccountToggleConnectedBotPaused = getattr(_fn, 'AccountToggleConnectedBotPaused', None)
DisablePeerConnectedBot = getattr(_fn, 'DisablePeerConnectedBot', getattr(_fn, 'AccountDisablePeerConnectedBot', None))
AccountDisablePeerConnectedBot = getattr(_fn, 'AccountDisablePeerConnectedBot', None)
UpdateBirthday = getattr(_fn, 'UpdateBirthday', getattr(_fn, 'AccountUpdateBirthday', None))
AccountUpdateBirthday = getattr(_fn, 'AccountUpdateBirthday', None)
CreateBusinessChatLink = getattr(_fn, 'CreateBusinessChatLink', getattr(_fn, 'AccountCreateBusinessChatLink', None))
AccountCreateBusinessChatLink = getattr(_fn, 'AccountCreateBusinessChatLink', None)
EditBusinessChatLink = getattr(_fn, 'EditBusinessChatLink', getattr(_fn, 'AccountEditBusinessChatLink', None))
AccountEditBusinessChatLink = getattr(_fn, 'AccountEditBusinessChatLink', None)
DeleteBusinessChatLink = getattr(_fn, 'DeleteBusinessChatLink', getattr(_fn, 'AccountDeleteBusinessChatLink', None))
AccountDeleteBusinessChatLink = getattr(_fn, 'AccountDeleteBusinessChatLink', None)
GetBusinessChatLinks = getattr(_fn, 'GetBusinessChatLinks', getattr(_fn, 'AccountGetBusinessChatLinks', None))
AccountGetBusinessChatLinks = getattr(_fn, 'AccountGetBusinessChatLinks', None)
ResolveBusinessChatLink = getattr(_fn, 'ResolveBusinessChatLink', getattr(_fn, 'AccountResolveBusinessChatLink', None))
AccountResolveBusinessChatLink = getattr(_fn, 'AccountResolveBusinessChatLink', None)
UpdatePersonalChannel = getattr(_fn, 'UpdatePersonalChannel', getattr(_fn, 'AccountUpdatePersonalChannel', None))
AccountUpdatePersonalChannel = getattr(_fn, 'AccountUpdatePersonalChannel', None)
ToggleSponsoredMessages = getattr(_fn, 'ToggleSponsoredMessages', getattr(_fn, 'AccountToggleSponsoredMessages', None))
AccountToggleSponsoredMessages = getattr(_fn, 'AccountToggleSponsoredMessages', None)
GetReactionsNotifySettings = getattr(_fn, 'GetReactionsNotifySettings', getattr(_fn, 'AccountGetReactionsNotifySettings', None))
AccountGetReactionsNotifySettings = getattr(_fn, 'AccountGetReactionsNotifySettings', None)
SetReactionsNotifySettings = getattr(_fn, 'SetReactionsNotifySettings', getattr(_fn, 'AccountSetReactionsNotifySettings', None))
AccountSetReactionsNotifySettings = getattr(_fn, 'AccountSetReactionsNotifySettings', None)
GetCollectibleEmojiStatuses = getattr(_fn, 'GetCollectibleEmojiStatuses', getattr(_fn, 'AccountGetCollectibleEmojiStatuses', None))
AccountGetCollectibleEmojiStatuses = getattr(_fn, 'AccountGetCollectibleEmojiStatuses', None)
GetPaidMessagesRevenue = getattr(_fn, 'GetPaidMessagesRevenue', getattr(_fn, 'AccountGetPaidMessagesRevenue', None))
AccountGetPaidMessagesRevenue = getattr(_fn, 'AccountGetPaidMessagesRevenue', None)
ToggleNoPaidMessagesException = getattr(_fn, 'ToggleNoPaidMessagesException', getattr(_fn, 'AccountToggleNoPaidMessagesException', None))
AccountToggleNoPaidMessagesException = getattr(_fn, 'AccountToggleNoPaidMessagesException', None)
SetMainProfileTab = getattr(_fn, 'SetMainProfileTab', getattr(_fn, 'AccountSetMainProfileTab', None))
AccountSetMainProfileTab = getattr(_fn, 'AccountSetMainProfileTab', None)
SaveMusic = getattr(_fn, 'SaveMusic', getattr(_fn, 'AccountSaveMusic', None))
AccountSaveMusic = getattr(_fn, 'AccountSaveMusic', None)
GetSavedMusicIds = getattr(_fn, 'GetSavedMusicIds', getattr(_fn, 'AccountGetSavedMusicIds', None))
AccountGetSavedMusicIds = getattr(_fn, 'AccountGetSavedMusicIds', None)
GetUniqueGiftChatThemes = getattr(_fn, 'GetUniqueGiftChatThemes', getattr(_fn, 'AccountGetUniqueGiftChatThemes', None))
AccountGetUniqueGiftChatThemes = getattr(_fn, 'AccountGetUniqueGiftChatThemes', None)
InitPasskeyRegistration = getattr(_fn, 'InitPasskeyRegistration', getattr(_fn, 'AccountInitPasskeyRegistration', None))
AccountInitPasskeyRegistration = getattr(_fn, 'AccountInitPasskeyRegistration', None)
RegisterPasskey = getattr(_fn, 'RegisterPasskey', getattr(_fn, 'AccountRegisterPasskey', None))
AccountRegisterPasskey = getattr(_fn, 'AccountRegisterPasskey', None)
GetPasskeys = getattr(_fn, 'GetPasskeys', getattr(_fn, 'AccountGetPasskeys', None))
AccountGetPasskeys = getattr(_fn, 'AccountGetPasskeys', None)
DeletePasskey = getattr(_fn, 'DeletePasskey', getattr(_fn, 'AccountDeletePasskey', None))
AccountDeletePasskey = getattr(_fn, 'AccountDeletePasskey', None)

__all__ = [
    "RegisterDevice",
    "AccountRegisterDevice",
    "UnregisterDevice",
    "AccountUnregisterDevice",
    "UpdateNotifySettings",
    "AccountUpdateNotifySettings",
    "GetNotifySettings",
    "AccountGetNotifySettings",
    "ResetNotifySettings",
    "AccountResetNotifySettings",
    "UpdateProfile",
    "AccountUpdateProfile",
    "UpdateStatus",
    "AccountUpdateStatus",
    "GetWallPapers",
    "AccountGetWallPapers",
    "ReportPeer",
    "AccountReportPeer",
    "CheckUsername",
    "AccountCheckUsername",
    "UpdateUsername",
    "AccountUpdateUsername",
    "GetPrivacy",
    "AccountGetPrivacy",
    "SetPrivacy",
    "AccountSetPrivacy",
    "DeleteAccount",
    "AccountDeleteAccount",
    "GetAccountTTL",
    "AccountGetAccountTTL",
    "SetAccountTTL",
    "AccountSetAccountTTL",
    "SendChangePhoneCode",
    "AccountSendChangePhoneCode",
    "ChangePhone",
    "AccountChangePhone",
    "UpdateDeviceLocked",
    "AccountUpdateDeviceLocked",
    "GetAuthorizations",
    "AccountGetAuthorizations",
    "ResetAuthorization",
    "AccountResetAuthorization",
    "GetPassword",
    "AccountGetPassword",
    "GetPasswordSettings",
    "AccountGetPasswordSettings",
    "UpdatePasswordSettings",
    "AccountUpdatePasswordSettings",
    "SendConfirmPhoneCode",
    "AccountSendConfirmPhoneCode",
    "ConfirmPhone",
    "AccountConfirmPhone",
    "GetTmpPassword",
    "AccountGetTmpPassword",
    "GetWebAuthorizations",
    "AccountGetWebAuthorizations",
    "ResetWebAuthorization",
    "AccountResetWebAuthorization",
    "ResetWebAuthorizations",
    "AccountResetWebAuthorizations",
    "GetAllSecureValues",
    "AccountGetAllSecureValues",
    "GetSecureValue",
    "AccountGetSecureValue",
    "SaveSecureValue",
    "AccountSaveSecureValue",
    "DeleteSecureValue",
    "AccountDeleteSecureValue",
    "GetAuthorizationForm",
    "AccountGetAuthorizationForm",
    "AcceptAuthorization",
    "AccountAcceptAuthorization",
    "SendVerifyPhoneCode",
    "AccountSendVerifyPhoneCode",
    "VerifyPhone",
    "AccountVerifyPhone",
    "SendVerifyEmailCode",
    "AccountSendVerifyEmailCode",
    "VerifyEmail",
    "AccountVerifyEmail",
    "InitTakeoutSession",
    "AccountInitTakeoutSession",
    "FinishTakeoutSession",
    "AccountFinishTakeoutSession",
    "ConfirmPasswordEmail",
    "AccountConfirmPasswordEmail",
    "ResendPasswordEmail",
    "AccountResendPasswordEmail",
    "CancelPasswordEmail",
    "AccountCancelPasswordEmail",
    "GetContactSignUpNotification",
    "AccountGetContactSignUpNotification",
    "SetContactSignUpNotification",
    "AccountSetContactSignUpNotification",
    "GetNotifyExceptions",
    "AccountGetNotifyExceptions",
    "GetWallPaper",
    "AccountGetWallPaper",
    "UploadWallPaper",
    "AccountUploadWallPaper",
    "SaveWallPaper",
    "AccountSaveWallPaper",
    "InstallWallPaper",
    "AccountInstallWallPaper",
    "ResetWallPapers",
    "AccountResetWallPapers",
    "GetAutoDownloadSettings",
    "AccountGetAutoDownloadSettings",
    "SaveAutoDownloadSettings",
    "AccountSaveAutoDownloadSettings",
    "UploadTheme",
    "AccountUploadTheme",
    "CreateTheme",
    "AccountCreateTheme",
    "UpdateTheme",
    "AccountUpdateTheme",
    "SaveTheme",
    "AccountSaveTheme",
    "InstallTheme",
    "AccountInstallTheme",
    "GetTheme",
    "AccountGetTheme",
    "GetThemes",
    "AccountGetThemes",
    "SetContentSettings",
    "AccountSetContentSettings",
    "GetContentSettings",
    "AccountGetContentSettings",
    "GetMultiWallPapers",
    "AccountGetMultiWallPapers",
    "GetGlobalPrivacySettings",
    "AccountGetGlobalPrivacySettings",
    "SetGlobalPrivacySettings",
    "AccountSetGlobalPrivacySettings",
    "ReportProfilePhoto",
    "AccountReportProfilePhoto",
    "ResetPassword",
    "AccountResetPassword",
    "DeclinePasswordReset",
    "AccountDeclinePasswordReset",
    "GetChatThemes",
    "AccountGetChatThemes",
    "SetAuthorizationTTL",
    "AccountSetAuthorizationTTL",
    "ChangeAuthorizationSettings",
    "AccountChangeAuthorizationSettings",
    "GetSavedRingtones",
    "AccountGetSavedRingtones",
    "SaveRingtone",
    "AccountSaveRingtone",
    "UploadRingtone",
    "AccountUploadRingtone",
    "UpdateEmojiStatus",
    "AccountUpdateEmojiStatus",
    "GetDefaultEmojiStatuses",
    "AccountGetDefaultEmojiStatuses",
    "GetRecentEmojiStatuses",
    "AccountGetRecentEmojiStatuses",
    "ClearRecentEmojiStatuses",
    "AccountClearRecentEmojiStatuses",
    "ReorderUsernames",
    "AccountReorderUsernames",
    "ToggleUsername",
    "AccountToggleUsername",
    "GetDefaultProfilePhotoEmojis",
    "AccountGetDefaultProfilePhotoEmojis",
    "GetDefaultGroupPhotoEmojis",
    "AccountGetDefaultGroupPhotoEmojis",
    "GetAutoSaveSettings",
    "AccountGetAutoSaveSettings",
    "SaveAutoSaveSettings",
    "AccountSaveAutoSaveSettings",
    "DeleteAutoSaveExceptions",
    "AccountDeleteAutoSaveExceptions",
    "InvalidateSignInCodes",
    "AccountInvalidateSignInCodes",
    "UpdateColor",
    "AccountUpdateColor",
    "GetDefaultBackgroundEmojis",
    "AccountGetDefaultBackgroundEmojis",
    "GetChannelDefaultEmojiStatuses",
    "AccountGetChannelDefaultEmojiStatuses",
    "GetChannelRestrictedStatusEmojis",
    "AccountGetChannelRestrictedStatusEmojis",
    "UpdateBusinessWorkHours",
    "AccountUpdateBusinessWorkHours",
    "UpdateBusinessLocation",
    "AccountUpdateBusinessLocation",
    "UpdateBusinessGreetingMessage",
    "AccountUpdateBusinessGreetingMessage",
    "UpdateBusinessAwayMessage",
    "AccountUpdateBusinessAwayMessage",
    "UpdateConnectedBot",
    "AccountUpdateConnectedBot",
    "GetConnectedBots",
    "AccountGetConnectedBots",
    "GetBotBusinessConnection",
    "AccountGetBotBusinessConnection",
    "UpdateBusinessIntro",
    "AccountUpdateBusinessIntro",
    "ToggleConnectedBotPaused",
    "AccountToggleConnectedBotPaused",
    "DisablePeerConnectedBot",
    "AccountDisablePeerConnectedBot",
    "UpdateBirthday",
    "AccountUpdateBirthday",
    "CreateBusinessChatLink",
    "AccountCreateBusinessChatLink",
    "EditBusinessChatLink",
    "AccountEditBusinessChatLink",
    "DeleteBusinessChatLink",
    "AccountDeleteBusinessChatLink",
    "GetBusinessChatLinks",
    "AccountGetBusinessChatLinks",
    "ResolveBusinessChatLink",
    "AccountResolveBusinessChatLink",
    "UpdatePersonalChannel",
    "AccountUpdatePersonalChannel",
    "ToggleSponsoredMessages",
    "AccountToggleSponsoredMessages",
    "GetReactionsNotifySettings",
    "AccountGetReactionsNotifySettings",
    "SetReactionsNotifySettings",
    "AccountSetReactionsNotifySettings",
    "GetCollectibleEmojiStatuses",
    "AccountGetCollectibleEmojiStatuses",
    "GetPaidMessagesRevenue",
    "AccountGetPaidMessagesRevenue",
    "ToggleNoPaidMessagesException",
    "AccountToggleNoPaidMessagesException",
    "SetMainProfileTab",
    "AccountSetMainProfileTab",
    "SaveMusic",
    "AccountSaveMusic",
    "GetSavedMusicIds",
    "AccountGetSavedMusicIds",
    "GetUniqueGiftChatThemes",
    "AccountGetUniqueGiftChatThemes",
    "InitPasskeyRegistration",
    "AccountInitPasskeyRegistration",
    "RegisterPasskey",
    "AccountRegisterPasskey",
    "GetPasskeys",
    "AccountGetPasskeys",
    "DeletePasskey",
    "AccountDeletePasskey"
]
