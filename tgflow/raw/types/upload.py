from ...tl import types as _tp


File = getattr(_tp, 'UploadFile', getattr(_tp, 'File', None))
UploadFile = getattr(_tp, 'UploadFile', None)
FileCdnRedirect = getattr(_tp, 'UploadFileCdnRedirect', getattr(_tp, 'FileCdnRedirect', None))
UploadFileCdnRedirect = getattr(_tp, 'UploadFileCdnRedirect', None)
WebFile = getattr(_tp, 'UploadWebFile', getattr(_tp, 'WebFile', None))
UploadWebFile = getattr(_tp, 'UploadWebFile', None)
CdnFileReuploadNeeded = getattr(_tp, 'UploadCdnFileReuploadNeeded', getattr(_tp, 'CdnFileReuploadNeeded', None))
UploadCdnFileReuploadNeeded = getattr(_tp, 'UploadCdnFileReuploadNeeded', None)
CdnFile = getattr(_tp, 'UploadCdnFile', getattr(_tp, 'CdnFile', None))
UploadCdnFile = getattr(_tp, 'UploadCdnFile', None)

__all__ = [
    "File",
    "UploadFile",
    "FileCdnRedirect",
    "UploadFileCdnRedirect",
    "WebFile",
    "UploadWebFile",
    "CdnFileReuploadNeeded",
    "UploadCdnFileReuploadNeeded",
    "CdnFile",
    "UploadCdnFile"
]
