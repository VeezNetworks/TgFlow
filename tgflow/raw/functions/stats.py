from ...tl import functions as _fn


GetBroadcastStats = getattr(_fn, 'GetBroadcastStats', getattr(_fn, 'StatsGetBroadcastStats', None))
StatsGetBroadcastStats = getattr(_fn, 'StatsGetBroadcastStats', None)
LoadAsyncGraph = getattr(_fn, 'LoadAsyncGraph', getattr(_fn, 'StatsLoadAsyncGraph', None))
StatsLoadAsyncGraph = getattr(_fn, 'StatsLoadAsyncGraph', None)
GetMegagroupStats = getattr(_fn, 'GetMegagroupStats', getattr(_fn, 'StatsGetMegagroupStats', None))
StatsGetMegagroupStats = getattr(_fn, 'StatsGetMegagroupStats', None)
GetMessagePublicForwards = getattr(_fn, 'GetMessagePublicForwards', getattr(_fn, 'StatsGetMessagePublicForwards', None))
StatsGetMessagePublicForwards = getattr(_fn, 'StatsGetMessagePublicForwards', None)
GetMessageStats = getattr(_fn, 'GetMessageStats', getattr(_fn, 'StatsGetMessageStats', None))
StatsGetMessageStats = getattr(_fn, 'StatsGetMessageStats', None)
GetStoryStats = getattr(_fn, 'GetStoryStats', getattr(_fn, 'StatsGetStoryStats', None))
StatsGetStoryStats = getattr(_fn, 'StatsGetStoryStats', None)
GetStoryPublicForwards = getattr(_fn, 'GetStoryPublicForwards', getattr(_fn, 'StatsGetStoryPublicForwards', None))
StatsGetStoryPublicForwards = getattr(_fn, 'StatsGetStoryPublicForwards', None)
GetPollStats = getattr(_fn, 'GetPollStats', getattr(_fn, 'StatsGetPollStats', None))
StatsGetPollStats = getattr(_fn, 'StatsGetPollStats', None)

__all__ = [
    "GetBroadcastStats",
    "StatsGetBroadcastStats",
    "LoadAsyncGraph",
    "StatsLoadAsyncGraph",
    "GetMegagroupStats",
    "StatsGetMegagroupStats",
    "GetMessagePublicForwards",
    "StatsGetMessagePublicForwards",
    "GetMessageStats",
    "StatsGetMessageStats",
    "GetStoryStats",
    "StatsGetStoryStats",
    "GetStoryPublicForwards",
    "StatsGetStoryPublicForwards",
    "GetPollStats",
    "StatsGetPollStats"
]
