from ...tl import functions as _fn


SaveFilePart = getattr(_fn, 'SaveFilePart', getattr(_fn, 'UploadSaveFilePart', None))
UploadSaveFilePart = getattr(_fn, 'UploadSaveFilePart', None)
GetFile = getattr(_fn, 'GetFile', getattr(_fn, 'UploadGetFile', None))
UploadGetFile = getattr(_fn, 'UploadGetFile', None)
SaveBigFilePart = getattr(_fn, 'SaveBigFilePart', getattr(_fn, 'UploadSaveBigFilePart', None))
UploadSaveBigFilePart = getattr(_fn, 'UploadSaveBigFilePart', None)
GetWebFile = getattr(_fn, 'GetWebFile', getattr(_fn, 'UploadGetWebFile', None))
UploadGetWebFile = getattr(_fn, 'UploadGetWebFile', None)
GetCdnFile = getattr(_fn, 'GetCdnFile', getattr(_fn, 'UploadGetCdnFile', None))
UploadGetCdnFile = getattr(_fn, 'UploadGetCdnFile', None)
ReuploadCdnFile = getattr(_fn, 'ReuploadCdnFile', getattr(_fn, 'UploadReuploadCdnFile', None))
UploadReuploadCdnFile = getattr(_fn, 'UploadReuploadCdnFile', None)
GetCdnFileHashes = getattr(_fn, 'GetCdnFileHashes', getattr(_fn, 'UploadGetCdnFileHashes', None))
UploadGetCdnFileHashes = getattr(_fn, 'UploadGetCdnFileHashes', None)
GetFileHashes = getattr(_fn, 'GetFileHashes', getattr(_fn, 'UploadGetFileHashes', None))
UploadGetFileHashes = getattr(_fn, 'UploadGetFileHashes', None)

__all__ = [
    "SaveFilePart",
    "UploadSaveFilePart",
    "GetFile",
    "UploadGetFile",
    "SaveBigFilePart",
    "UploadSaveBigFilePart",
    "GetWebFile",
    "UploadGetWebFile",
    "GetCdnFile",
    "UploadGetCdnFile",
    "ReuploadCdnFile",
    "UploadReuploadCdnFile",
    "GetCdnFileHashes",
    "UploadGetCdnFileHashes",
    "GetFileHashes",
    "UploadGetFileHashes"
]
