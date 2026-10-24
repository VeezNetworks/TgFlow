from ...tl import types as _tp


FileUnknown = getattr(_tp, 'StorageFileUnknown', getattr(_tp, 'FileUnknown', None))
StorageFileUnknown = getattr(_tp, 'StorageFileUnknown', None)
FilePartial = getattr(_tp, 'StorageFilePartial', getattr(_tp, 'FilePartial', None))
StorageFilePartial = getattr(_tp, 'StorageFilePartial', None)
FileJpeg = getattr(_tp, 'StorageFileJpeg', getattr(_tp, 'FileJpeg', None))
StorageFileJpeg = getattr(_tp, 'StorageFileJpeg', None)
FileGif = getattr(_tp, 'StorageFileGif', getattr(_tp, 'FileGif', None))
StorageFileGif = getattr(_tp, 'StorageFileGif', None)
FilePng = getattr(_tp, 'StorageFilePng', getattr(_tp, 'FilePng', None))
StorageFilePng = getattr(_tp, 'StorageFilePng', None)
FilePdf = getattr(_tp, 'StorageFilePdf', getattr(_tp, 'FilePdf', None))
StorageFilePdf = getattr(_tp, 'StorageFilePdf', None)
FileMp3 = getattr(_tp, 'StorageFileMp3', getattr(_tp, 'FileMp3', None))
StorageFileMp3 = getattr(_tp, 'StorageFileMp3', None)
FileMov = getattr(_tp, 'StorageFileMov', getattr(_tp, 'FileMov', None))
StorageFileMov = getattr(_tp, 'StorageFileMov', None)
FileMp4 = getattr(_tp, 'StorageFileMp4', getattr(_tp, 'FileMp4', None))
StorageFileMp4 = getattr(_tp, 'StorageFileMp4', None)
FileWebp = getattr(_tp, 'StorageFileWebp', getattr(_tp, 'FileWebp', None))
StorageFileWebp = getattr(_tp, 'StorageFileWebp', None)

__all__ = [
    "FileUnknown",
    "StorageFileUnknown",
    "FilePartial",
    "StorageFilePartial",
    "FileJpeg",
    "StorageFileJpeg",
    "FileGif",
    "StorageFileGif",
    "FilePng",
    "StorageFilePng",
    "FilePdf",
    "StorageFilePdf",
    "FileMp3",
    "StorageFileMp3",
    "FileMov",
    "StorageFileMov",
    "FileMp4",
    "StorageFileMp4",
    "FileWebp",
    "StorageFileWebp"
]
