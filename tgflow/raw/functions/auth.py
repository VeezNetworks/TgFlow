from ...tl import functions as _fn


SendCode = getattr(_fn, 'SendCode', getattr(_fn, 'AuthSendCode', None))
AuthSendCode = getattr(_fn, 'AuthSendCode', None)
SignUp = getattr(_fn, 'SignUp', getattr(_fn, 'AuthSignUp', None))
AuthSignUp = getattr(_fn, 'AuthSignUp', None)
SignIn = getattr(_fn, 'SignIn', getattr(_fn, 'AuthSignIn', None))
AuthSignIn = getattr(_fn, 'AuthSignIn', None)
LogOut = getattr(_fn, 'LogOut', getattr(_fn, 'AuthLogOut', None))
AuthLogOut = getattr(_fn, 'AuthLogOut', None)
ResetAuthorizations = getattr(_fn, 'ResetAuthorizations', getattr(_fn, 'AuthResetAuthorizations', None))
AuthResetAuthorizations = getattr(_fn, 'AuthResetAuthorizations', None)
ExportAuthorization = getattr(_fn, 'ExportAuthorization', getattr(_fn, 'AuthExportAuthorization', None))
AuthExportAuthorization = getattr(_fn, 'AuthExportAuthorization', None)
ImportAuthorization = getattr(_fn, 'ImportAuthorization', getattr(_fn, 'AuthImportAuthorization', None))
AuthImportAuthorization = getattr(_fn, 'AuthImportAuthorization', None)
BindTempAuthKey = getattr(_fn, 'BindTempAuthKey', getattr(_fn, 'AuthBindTempAuthKey', None))
AuthBindTempAuthKey = getattr(_fn, 'AuthBindTempAuthKey', None)
ImportBotAuthorization = getattr(_fn, 'ImportBotAuthorization', getattr(_fn, 'AuthImportBotAuthorization', None))
AuthImportBotAuthorization = getattr(_fn, 'AuthImportBotAuthorization', None)
CheckPassword = getattr(_fn, 'CheckPassword', getattr(_fn, 'AuthCheckPassword', None))
AuthCheckPassword = getattr(_fn, 'AuthCheckPassword', None)
RequestPasswordRecovery = getattr(_fn, 'RequestPasswordRecovery', getattr(_fn, 'AuthRequestPasswordRecovery', None))
AuthRequestPasswordRecovery = getattr(_fn, 'AuthRequestPasswordRecovery', None)
RecoverPassword = getattr(_fn, 'RecoverPassword', getattr(_fn, 'AuthRecoverPassword', None))
AuthRecoverPassword = getattr(_fn, 'AuthRecoverPassword', None)
ResendCode = getattr(_fn, 'ResendCode', getattr(_fn, 'AuthResendCode', None))
AuthResendCode = getattr(_fn, 'AuthResendCode', None)
CancelCode = getattr(_fn, 'CancelCode', getattr(_fn, 'AuthCancelCode', None))
AuthCancelCode = getattr(_fn, 'AuthCancelCode', None)
DropTempAuthKeys = getattr(_fn, 'DropTempAuthKeys', getattr(_fn, 'AuthDropTempAuthKeys', None))
AuthDropTempAuthKeys = getattr(_fn, 'AuthDropTempAuthKeys', None)
ExportLoginToken = getattr(_fn, 'ExportLoginToken', getattr(_fn, 'AuthExportLoginToken', None))
AuthExportLoginToken = getattr(_fn, 'AuthExportLoginToken', None)
ImportLoginToken = getattr(_fn, 'ImportLoginToken', getattr(_fn, 'AuthImportLoginToken', None))
AuthImportLoginToken = getattr(_fn, 'AuthImportLoginToken', None)
AcceptLoginToken = getattr(_fn, 'AcceptLoginToken', getattr(_fn, 'AuthAcceptLoginToken', None))
AuthAcceptLoginToken = getattr(_fn, 'AuthAcceptLoginToken', None)
CheckRecoveryPassword = getattr(_fn, 'CheckRecoveryPassword', getattr(_fn, 'AuthCheckRecoveryPassword', None))
AuthCheckRecoveryPassword = getattr(_fn, 'AuthCheckRecoveryPassword', None)
ImportWebTokenAuthorization = getattr(_fn, 'ImportWebTokenAuthorization', getattr(_fn, 'AuthImportWebTokenAuthorization', None))
AuthImportWebTokenAuthorization = getattr(_fn, 'AuthImportWebTokenAuthorization', None)
RequestFirebaseSms = getattr(_fn, 'RequestFirebaseSms', getattr(_fn, 'AuthRequestFirebaseSms', None))
AuthRequestFirebaseSms = getattr(_fn, 'AuthRequestFirebaseSms', None)
ResetLoginEmail = getattr(_fn, 'ResetLoginEmail', getattr(_fn, 'AuthResetLoginEmail', None))
AuthResetLoginEmail = getattr(_fn, 'AuthResetLoginEmail', None)
ReportMissingCode = getattr(_fn, 'ReportMissingCode', getattr(_fn, 'AuthReportMissingCode', None))
AuthReportMissingCode = getattr(_fn, 'AuthReportMissingCode', None)
CheckPaidAuth = getattr(_fn, 'CheckPaidAuth', getattr(_fn, 'AuthCheckPaidAuth', None))
AuthCheckPaidAuth = getattr(_fn, 'AuthCheckPaidAuth', None)
InitPasskeyLogin = getattr(_fn, 'InitPasskeyLogin', getattr(_fn, 'AuthInitPasskeyLogin', None))
AuthInitPasskeyLogin = getattr(_fn, 'AuthInitPasskeyLogin', None)
FinishPasskeyLogin = getattr(_fn, 'FinishPasskeyLogin', getattr(_fn, 'AuthFinishPasskeyLogin', None))
AuthFinishPasskeyLogin = getattr(_fn, 'AuthFinishPasskeyLogin', None)

__all__ = [
    "SendCode",
    "AuthSendCode",
    "SignUp",
    "AuthSignUp",
    "SignIn",
    "AuthSignIn",
    "LogOut",
    "AuthLogOut",
    "ResetAuthorizations",
    "AuthResetAuthorizations",
    "ExportAuthorization",
    "AuthExportAuthorization",
    "ImportAuthorization",
    "AuthImportAuthorization",
    "BindTempAuthKey",
    "AuthBindTempAuthKey",
    "ImportBotAuthorization",
    "AuthImportBotAuthorization",
    "CheckPassword",
    "AuthCheckPassword",
    "RequestPasswordRecovery",
    "AuthRequestPasswordRecovery",
    "RecoverPassword",
    "AuthRecoverPassword",
    "ResendCode",
    "AuthResendCode",
    "CancelCode",
    "AuthCancelCode",
    "DropTempAuthKeys",
    "AuthDropTempAuthKeys",
    "ExportLoginToken",
    "AuthExportLoginToken",
    "ImportLoginToken",
    "AuthImportLoginToken",
    "AcceptLoginToken",
    "AuthAcceptLoginToken",
    "CheckRecoveryPassword",
    "AuthCheckRecoveryPassword",
    "ImportWebTokenAuthorization",
    "AuthImportWebTokenAuthorization",
    "RequestFirebaseSms",
    "AuthRequestFirebaseSms",
    "ResetLoginEmail",
    "AuthResetLoginEmail",
    "ReportMissingCode",
    "AuthReportMissingCode",
    "CheckPaidAuth",
    "AuthCheckPaidAuth",
    "InitPasskeyLogin",
    "AuthInitPasskeyLogin",
    "FinishPasskeyLogin",
    "AuthFinishPasskeyLogin"
]
