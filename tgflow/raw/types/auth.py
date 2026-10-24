from ...tl import types as _tp


SentCode = getattr(_tp, 'AuthSentCode', getattr(_tp, 'SentCode', None))
AuthSentCode = getattr(_tp, 'AuthSentCode', None)
SentCodeSuccess = getattr(_tp, 'AuthSentCodeSuccess', getattr(_tp, 'SentCodeSuccess', None))
AuthSentCodeSuccess = getattr(_tp, 'AuthSentCodeSuccess', None)
SentCodePaymentRequired = getattr(_tp, 'AuthSentCodePaymentRequired', getattr(_tp, 'SentCodePaymentRequired', None))
AuthSentCodePaymentRequired = getattr(_tp, 'AuthSentCodePaymentRequired', None)
Authorization = getattr(_tp, 'AuthAuthorization', getattr(_tp, 'Authorization', None))
AuthAuthorization = getattr(_tp, 'AuthAuthorization', None)
AuthorizationSignUpRequired = getattr(_tp, 'AuthAuthorizationSignUpRequired', getattr(_tp, 'AuthorizationSignUpRequired', None))
AuthAuthorizationSignUpRequired = getattr(_tp, 'AuthAuthorizationSignUpRequired', None)
ExportedAuthorization = getattr(_tp, 'AuthExportedAuthorization', getattr(_tp, 'ExportedAuthorization', None))
AuthExportedAuthorization = getattr(_tp, 'AuthExportedAuthorization', None)
PasswordRecovery = getattr(_tp, 'AuthPasswordRecovery', getattr(_tp, 'PasswordRecovery', None))
AuthPasswordRecovery = getattr(_tp, 'AuthPasswordRecovery', None)
CodeTypeSms = getattr(_tp, 'AuthCodeTypeSms', getattr(_tp, 'CodeTypeSms', None))
AuthCodeTypeSms = getattr(_tp, 'AuthCodeTypeSms', None)
CodeTypeCall = getattr(_tp, 'AuthCodeTypeCall', getattr(_tp, 'CodeTypeCall', None))
AuthCodeTypeCall = getattr(_tp, 'AuthCodeTypeCall', None)
CodeTypeFlashCall = getattr(_tp, 'AuthCodeTypeFlashCall', getattr(_tp, 'CodeTypeFlashCall', None))
AuthCodeTypeFlashCall = getattr(_tp, 'AuthCodeTypeFlashCall', None)
CodeTypeMissedCall = getattr(_tp, 'AuthCodeTypeMissedCall', getattr(_tp, 'CodeTypeMissedCall', None))
AuthCodeTypeMissedCall = getattr(_tp, 'AuthCodeTypeMissedCall', None)
CodeTypeFragmentSms = getattr(_tp, 'AuthCodeTypeFragmentSms', getattr(_tp, 'CodeTypeFragmentSms', None))
AuthCodeTypeFragmentSms = getattr(_tp, 'AuthCodeTypeFragmentSms', None)
SentCodeTypeApp = getattr(_tp, 'AuthSentCodeTypeApp', getattr(_tp, 'SentCodeTypeApp', None))
AuthSentCodeTypeApp = getattr(_tp, 'AuthSentCodeTypeApp', None)
SentCodeTypeSms = getattr(_tp, 'AuthSentCodeTypeSms', getattr(_tp, 'SentCodeTypeSms', None))
AuthSentCodeTypeSms = getattr(_tp, 'AuthSentCodeTypeSms', None)
SentCodeTypeCall = getattr(_tp, 'AuthSentCodeTypeCall', getattr(_tp, 'SentCodeTypeCall', None))
AuthSentCodeTypeCall = getattr(_tp, 'AuthSentCodeTypeCall', None)
SentCodeTypeFlashCall = getattr(_tp, 'AuthSentCodeTypeFlashCall', getattr(_tp, 'SentCodeTypeFlashCall', None))
AuthSentCodeTypeFlashCall = getattr(_tp, 'AuthSentCodeTypeFlashCall', None)
SentCodeTypeMissedCall = getattr(_tp, 'AuthSentCodeTypeMissedCall', getattr(_tp, 'SentCodeTypeMissedCall', None))
AuthSentCodeTypeMissedCall = getattr(_tp, 'AuthSentCodeTypeMissedCall', None)
SentCodeTypeEmailCode = getattr(_tp, 'AuthSentCodeTypeEmailCode', getattr(_tp, 'SentCodeTypeEmailCode', None))
AuthSentCodeTypeEmailCode = getattr(_tp, 'AuthSentCodeTypeEmailCode', None)
SentCodeTypeSetUpEmailRequired = getattr(_tp, 'AuthSentCodeTypeSetUpEmailRequired', getattr(_tp, 'SentCodeTypeSetUpEmailRequired', None))
AuthSentCodeTypeSetUpEmailRequired = getattr(_tp, 'AuthSentCodeTypeSetUpEmailRequired', None)
SentCodeTypeFragmentSms = getattr(_tp, 'AuthSentCodeTypeFragmentSms', getattr(_tp, 'SentCodeTypeFragmentSms', None))
AuthSentCodeTypeFragmentSms = getattr(_tp, 'AuthSentCodeTypeFragmentSms', None)
SentCodeTypeFirebaseSms = getattr(_tp, 'AuthSentCodeTypeFirebaseSms', getattr(_tp, 'SentCodeTypeFirebaseSms', None))
AuthSentCodeTypeFirebaseSms = getattr(_tp, 'AuthSentCodeTypeFirebaseSms', None)
SentCodeTypeSmsWord = getattr(_tp, 'AuthSentCodeTypeSmsWord', getattr(_tp, 'SentCodeTypeSmsWord', None))
AuthSentCodeTypeSmsWord = getattr(_tp, 'AuthSentCodeTypeSmsWord', None)
SentCodeTypeSmsPhrase = getattr(_tp, 'AuthSentCodeTypeSmsPhrase', getattr(_tp, 'SentCodeTypeSmsPhrase', None))
AuthSentCodeTypeSmsPhrase = getattr(_tp, 'AuthSentCodeTypeSmsPhrase', None)
LoginToken = getattr(_tp, 'AuthLoginToken', getattr(_tp, 'LoginToken', None))
AuthLoginToken = getattr(_tp, 'AuthLoginToken', None)
LoginTokenMigrateTo = getattr(_tp, 'AuthLoginTokenMigrateTo', getattr(_tp, 'LoginTokenMigrateTo', None))
AuthLoginTokenMigrateTo = getattr(_tp, 'AuthLoginTokenMigrateTo', None)
LoginTokenSuccess = getattr(_tp, 'AuthLoginTokenSuccess', getattr(_tp, 'LoginTokenSuccess', None))
AuthLoginTokenSuccess = getattr(_tp, 'AuthLoginTokenSuccess', None)
LoggedOut = getattr(_tp, 'AuthLoggedOut', getattr(_tp, 'LoggedOut', None))
AuthLoggedOut = getattr(_tp, 'AuthLoggedOut', None)
PasskeyLoginOptions = getattr(_tp, 'AuthPasskeyLoginOptions', getattr(_tp, 'PasskeyLoginOptions', None))
AuthPasskeyLoginOptions = getattr(_tp, 'AuthPasskeyLoginOptions', None)

__all__ = [
    "SentCode",
    "AuthSentCode",
    "SentCodeSuccess",
    "AuthSentCodeSuccess",
    "SentCodePaymentRequired",
    "AuthSentCodePaymentRequired",
    "Authorization",
    "AuthAuthorization",
    "AuthorizationSignUpRequired",
    "AuthAuthorizationSignUpRequired",
    "ExportedAuthorization",
    "AuthExportedAuthorization",
    "PasswordRecovery",
    "AuthPasswordRecovery",
    "CodeTypeSms",
    "AuthCodeTypeSms",
    "CodeTypeCall",
    "AuthCodeTypeCall",
    "CodeTypeFlashCall",
    "AuthCodeTypeFlashCall",
    "CodeTypeMissedCall",
    "AuthCodeTypeMissedCall",
    "CodeTypeFragmentSms",
    "AuthCodeTypeFragmentSms",
    "SentCodeTypeApp",
    "AuthSentCodeTypeApp",
    "SentCodeTypeSms",
    "AuthSentCodeTypeSms",
    "SentCodeTypeCall",
    "AuthSentCodeTypeCall",
    "SentCodeTypeFlashCall",
    "AuthSentCodeTypeFlashCall",
    "SentCodeTypeMissedCall",
    "AuthSentCodeTypeMissedCall",
    "SentCodeTypeEmailCode",
    "AuthSentCodeTypeEmailCode",
    "SentCodeTypeSetUpEmailRequired",
    "AuthSentCodeTypeSetUpEmailRequired",
    "SentCodeTypeFragmentSms",
    "AuthSentCodeTypeFragmentSms",
    "SentCodeTypeFirebaseSms",
    "AuthSentCodeTypeFirebaseSms",
    "SentCodeTypeSmsWord",
    "AuthSentCodeTypeSmsWord",
    "SentCodeTypeSmsPhrase",
    "AuthSentCodeTypeSmsPhrase",
    "LoginToken",
    "AuthLoginToken",
    "LoginTokenMigrateTo",
    "AuthLoginTokenMigrateTo",
    "LoginTokenSuccess",
    "AuthLoginTokenSuccess",
    "LoggedOut",
    "AuthLoggedOut",
    "PasskeyLoginOptions",
    "AuthPasskeyLoginOptions"
]
