from ...tl import types as _tp


UserFull = getattr(_tp, 'UsersUserFull', getattr(_tp, 'UserFull', None))
UsersUserFull = getattr(_tp, 'UsersUserFull', None)
Users = getattr(_tp, 'UsersUsers', getattr(_tp, 'Users', None))
UsersUsers = getattr(_tp, 'UsersUsers', None)
UsersSlice = getattr(_tp, 'UsersUsersSlice', getattr(_tp, 'UsersSlice', None))
UsersUsersSlice = getattr(_tp, 'UsersUsersSlice', None)
SavedMusicNotModified = getattr(_tp, 'UsersSavedMusicNotModified', getattr(_tp, 'SavedMusicNotModified', None))
UsersSavedMusicNotModified = getattr(_tp, 'UsersSavedMusicNotModified', None)
SavedMusic = getattr(_tp, 'UsersSavedMusic', getattr(_tp, 'SavedMusic', None))
UsersSavedMusic = getattr(_tp, 'UsersSavedMusic', None)

__all__ = [
    "UserFull",
    "UsersUserFull",
    "Users",
    "UsersUsers",
    "UsersSlice",
    "UsersUsersSlice",
    "SavedMusicNotModified",
    "UsersSavedMusicNotModified",
    "SavedMusic",
    "UsersSavedMusic"
]
