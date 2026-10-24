from ...tl import types as _tp


State = getattr(_tp, 'UpdatesState', getattr(_tp, 'State', None))
UpdatesState = getattr(_tp, 'UpdatesState', None)
DifferenceEmpty = getattr(_tp, 'UpdatesDifferenceEmpty', getattr(_tp, 'DifferenceEmpty', None))
UpdatesDifferenceEmpty = getattr(_tp, 'UpdatesDifferenceEmpty', None)
Difference = getattr(_tp, 'UpdatesDifference', getattr(_tp, 'Difference', None))
UpdatesDifference = getattr(_tp, 'UpdatesDifference', None)
DifferenceSlice = getattr(_tp, 'UpdatesDifferenceSlice', getattr(_tp, 'DifferenceSlice', None))
UpdatesDifferenceSlice = getattr(_tp, 'UpdatesDifferenceSlice', None)
DifferenceTooLong = getattr(_tp, 'UpdatesDifferenceTooLong', getattr(_tp, 'DifferenceTooLong', None))
UpdatesDifferenceTooLong = getattr(_tp, 'UpdatesDifferenceTooLong', None)
ChannelDifferenceEmpty = getattr(_tp, 'UpdatesChannelDifferenceEmpty', getattr(_tp, 'ChannelDifferenceEmpty', None))
UpdatesChannelDifferenceEmpty = getattr(_tp, 'UpdatesChannelDifferenceEmpty', None)
ChannelDifferenceTooLong = getattr(_tp, 'UpdatesChannelDifferenceTooLong', getattr(_tp, 'ChannelDifferenceTooLong', None))
UpdatesChannelDifferenceTooLong = getattr(_tp, 'UpdatesChannelDifferenceTooLong', None)
ChannelDifference = getattr(_tp, 'UpdatesChannelDifference', getattr(_tp, 'ChannelDifference', None))
UpdatesChannelDifference = getattr(_tp, 'UpdatesChannelDifference', None)

__all__ = [
    "State",
    "UpdatesState",
    "DifferenceEmpty",
    "UpdatesDifferenceEmpty",
    "Difference",
    "UpdatesDifference",
    "DifferenceSlice",
    "UpdatesDifferenceSlice",
    "DifferenceTooLong",
    "UpdatesDifferenceTooLong",
    "ChannelDifferenceEmpty",
    "UpdatesChannelDifferenceEmpty",
    "ChannelDifferenceTooLong",
    "UpdatesChannelDifferenceTooLong",
    "ChannelDifference",
    "UpdatesChannelDifference"
]
