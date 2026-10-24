from ...tl import functions as _fn


UpdateProfilePhoto = getattr(_fn, 'UpdateProfilePhoto', getattr(_fn, 'PhotosUpdateProfilePhoto', None))
PhotosUpdateProfilePhoto = getattr(_fn, 'PhotosUpdateProfilePhoto', None)
UploadProfilePhoto = getattr(_fn, 'UploadProfilePhoto', getattr(_fn, 'PhotosUploadProfilePhoto', None))
PhotosUploadProfilePhoto = getattr(_fn, 'PhotosUploadProfilePhoto', None)
DeletePhotos = getattr(_fn, 'DeletePhotos', getattr(_fn, 'PhotosDeletePhotos', None))
PhotosDeletePhotos = getattr(_fn, 'PhotosDeletePhotos', None)
GetUserPhotos = getattr(_fn, 'GetUserPhotos', getattr(_fn, 'PhotosGetUserPhotos', None))
PhotosGetUserPhotos = getattr(_fn, 'PhotosGetUserPhotos', None)
UploadContactProfilePhoto = getattr(_fn, 'UploadContactProfilePhoto', getattr(_fn, 'PhotosUploadContactProfilePhoto', None))
PhotosUploadContactProfilePhoto = getattr(_fn, 'PhotosUploadContactProfilePhoto', None)

__all__ = [
    "UpdateProfilePhoto",
    "PhotosUpdateProfilePhoto",
    "UploadProfilePhoto",
    "PhotosUploadProfilePhoto",
    "DeletePhotos",
    "PhotosDeletePhotos",
    "GetUserPhotos",
    "PhotosGetUserPhotos",
    "UploadContactProfilePhoto",
    "PhotosUploadContactProfilePhoto"
]
