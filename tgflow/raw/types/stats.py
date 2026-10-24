from ...tl import types as _tp


BroadcastStats = getattr(_tp, 'StatsBroadcastStats', getattr(_tp, 'BroadcastStats', None))
StatsBroadcastStats = getattr(_tp, 'StatsBroadcastStats', None)
MegagroupStats = getattr(_tp, 'StatsMegagroupStats', getattr(_tp, 'MegagroupStats', None))
StatsMegagroupStats = getattr(_tp, 'StatsMegagroupStats', None)
MessageStats = getattr(_tp, 'StatsMessageStats', getattr(_tp, 'MessageStats', None))
StatsMessageStats = getattr(_tp, 'StatsMessageStats', None)
StoryStats = getattr(_tp, 'StatsStoryStats', getattr(_tp, 'StoryStats', None))
StatsStoryStats = getattr(_tp, 'StatsStoryStats', None)
PublicForwards = getattr(_tp, 'StatsPublicForwards', getattr(_tp, 'PublicForwards', None))
StatsPublicForwards = getattr(_tp, 'StatsPublicForwards', None)
PollStats = getattr(_tp, 'StatsPollStats', getattr(_tp, 'PollStats', None))
StatsPollStats = getattr(_tp, 'StatsPollStats', None)

__all__ = [
    "BroadcastStats",
    "StatsBroadcastStats",
    "MegagroupStats",
    "StatsMegagroupStats",
    "MessageStats",
    "StatsMessageStats",
    "StoryStats",
    "StatsStoryStats",
    "PublicForwards",
    "StatsPublicForwards",
    "PollStats",
    "StatsPollStats"
]
