from ...tl import types as _tp


Photos = getattr(_tp, 'PhotosPhotos', getattr(_tp, 'Photos', None))
PhotosPhotos = getattr(_tp, 'PhotosPhotos', None)
PhotosSlice = getattr(_tp, 'PhotosPhotosSlice', getattr(_tp, 'PhotosSlice', None))
PhotosPhotosSlice = getattr(_tp, 'PhotosPhotosSlice', None)
Photo = getattr(_tp, 'PhotosPhoto', getattr(_tp, 'Photo', None))
PhotosPhoto = getattr(_tp, 'PhotosPhoto', None)

__all__ = [
    "Photos",
    "PhotosPhotos",
    "PhotosSlice",
    "PhotosPhotosSlice",
    "Photo",
    "PhotosPhoto"
]
