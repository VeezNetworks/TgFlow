from ...tl import functions as _fn


CreateTone = getattr(_fn, 'CreateTone', getattr(_fn, 'AicomposeCreateTone', None))
AicomposeCreateTone = getattr(_fn, 'AicomposeCreateTone', None)
UpdateTone = getattr(_fn, 'UpdateTone', getattr(_fn, 'AicomposeUpdateTone', None))
AicomposeUpdateTone = getattr(_fn, 'AicomposeUpdateTone', None)
SaveTone = getattr(_fn, 'SaveTone', getattr(_fn, 'AicomposeSaveTone', None))
AicomposeSaveTone = getattr(_fn, 'AicomposeSaveTone', None)
DeleteTone = getattr(_fn, 'DeleteTone', getattr(_fn, 'AicomposeDeleteTone', None))
AicomposeDeleteTone = getattr(_fn, 'AicomposeDeleteTone', None)
GetTone = getattr(_fn, 'GetTone', getattr(_fn, 'AicomposeGetTone', None))
AicomposeGetTone = getattr(_fn, 'AicomposeGetTone', None)
GetTones = getattr(_fn, 'GetTones', getattr(_fn, 'AicomposeGetTones', None))
AicomposeGetTones = getattr(_fn, 'AicomposeGetTones', None)
GetToneExample = getattr(_fn, 'GetToneExample', getattr(_fn, 'AicomposeGetToneExample', None))
AicomposeGetToneExample = getattr(_fn, 'AicomposeGetToneExample', None)

__all__ = [
    "CreateTone",
    "AicomposeCreateTone",
    "UpdateTone",
    "AicomposeUpdateTone",
    "SaveTone",
    "AicomposeSaveTone",
    "DeleteTone",
    "AicomposeDeleteTone",
    "GetTone",
    "AicomposeGetTone",
    "GetTones",
    "AicomposeGetTones",
    "GetToneExample",
    "AicomposeGetToneExample"
]
