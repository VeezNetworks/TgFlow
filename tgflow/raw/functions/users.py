from ...tl import functions as _fn


GetUsers = getattr(_fn, 'GetUsers', getattr(_fn, 'UsersGetUsers', None))
UsersGetUsers = getattr(_fn, 'UsersGetUsers', None)
GetFullUser = getattr(_fn, 'GetFullUser', getattr(_fn, 'UsersGetFullUser', None))
UsersGetFullUser = getattr(_fn, 'UsersGetFullUser', None)
SetSecureValueErrors = getattr(_fn, 'SetSecureValueErrors', getattr(_fn, 'UsersSetSecureValueErrors', None))
UsersSetSecureValueErrors = getattr(_fn, 'UsersSetSecureValueErrors', None)
GetRequirementsToContact = getattr(_fn, 'GetRequirementsToContact', getattr(_fn, 'UsersGetRequirementsToContact', None))
UsersGetRequirementsToContact = getattr(_fn, 'UsersGetRequirementsToContact', None)
GetSavedMusic = getattr(_fn, 'GetSavedMusic', getattr(_fn, 'UsersGetSavedMusic', None))
UsersGetSavedMusic = getattr(_fn, 'UsersGetSavedMusic', None)
GetSavedMusicByID = getattr(_fn, 'GetSavedMusicByID', getattr(_fn, 'UsersGetSavedMusicByID', None))
UsersGetSavedMusicByID = getattr(_fn, 'UsersGetSavedMusicByID', None)
SuggestBirthday = getattr(_fn, 'SuggestBirthday', getattr(_fn, 'UsersSuggestBirthday', None))
UsersSuggestBirthday = getattr(_fn, 'UsersSuggestBirthday', None)

__all__ = [
    "GetUsers",
    "UsersGetUsers",
    "GetFullUser",
    "UsersGetFullUser",
    "SetSecureValueErrors",
    "UsersSetSecureValueErrors",
    "GetRequirementsToContact",
    "UsersGetRequirementsToContact",
    "GetSavedMusic",
    "UsersGetSavedMusic",
    "GetSavedMusicByID",
    "UsersGetSavedMusicByID",
    "SuggestBirthday",
    "UsersSuggestBirthday"
]
