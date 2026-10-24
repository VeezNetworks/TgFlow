from ...tl import functions as _fn


GetState = getattr(_fn, 'GetState', getattr(_fn, 'UpdatesGetState', None))
UpdatesGetState = getattr(_fn, 'UpdatesGetState', None)
GetDifference = getattr(_fn, 'GetDifference', getattr(_fn, 'UpdatesGetDifference', None))
UpdatesGetDifference = getattr(_fn, 'UpdatesGetDifference', None)
GetChannelDifference = getattr(_fn, 'GetChannelDifference', getattr(_fn, 'UpdatesGetChannelDifference', None))
UpdatesGetChannelDifference = getattr(_fn, 'UpdatesGetChannelDifference', None)

__all__ = [
    "GetState",
    "UpdatesGetState",
    "GetDifference",
    "UpdatesGetDifference",
    "GetChannelDifference",
    "UpdatesGetChannelDifference"
]
