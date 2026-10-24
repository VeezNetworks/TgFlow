from ...tl import types as _tp


EligibleToJoin = getattr(_tp, 'SmsjobsEligibleToJoin', getattr(_tp, 'EligibleToJoin', None))
SmsjobsEligibleToJoin = getattr(_tp, 'SmsjobsEligibleToJoin', None)
Status = getattr(_tp, 'SmsjobsStatus', getattr(_tp, 'Status', None))
SmsjobsStatus = getattr(_tp, 'SmsjobsStatus', None)

__all__ = [
    "EligibleToJoin",
    "SmsjobsEligibleToJoin",
    "Status",
    "SmsjobsStatus"
]
