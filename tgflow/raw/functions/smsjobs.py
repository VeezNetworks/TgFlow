from ...tl import functions as _fn


IsEligibleToJoin = getattr(_fn, 'IsEligibleToJoin', getattr(_fn, 'SmsjobsIsEligibleToJoin', None))
SmsjobsIsEligibleToJoin = getattr(_fn, 'SmsjobsIsEligibleToJoin', None)
Join = getattr(_fn, 'Join', getattr(_fn, 'SmsjobsJoin', None))
SmsjobsJoin = getattr(_fn, 'SmsjobsJoin', None)
Leave = getattr(_fn, 'Leave', getattr(_fn, 'SmsjobsLeave', None))
SmsjobsLeave = getattr(_fn, 'SmsjobsLeave', None)
UpdateSettings = getattr(_fn, 'UpdateSettings', getattr(_fn, 'SmsjobsUpdateSettings', None))
SmsjobsUpdateSettings = getattr(_fn, 'SmsjobsUpdateSettings', None)
GetStatus = getattr(_fn, 'GetStatus', getattr(_fn, 'SmsjobsGetStatus', None))
SmsjobsGetStatus = getattr(_fn, 'SmsjobsGetStatus', None)
GetSmsJob = getattr(_fn, 'GetSmsJob', getattr(_fn, 'SmsjobsGetSmsJob', None))
SmsjobsGetSmsJob = getattr(_fn, 'SmsjobsGetSmsJob', None)
FinishJob = getattr(_fn, 'FinishJob', getattr(_fn, 'SmsjobsFinishJob', None))
SmsjobsFinishJob = getattr(_fn, 'SmsjobsFinishJob', None)

__all__ = [
    "IsEligibleToJoin",
    "SmsjobsIsEligibleToJoin",
    "Join",
    "SmsjobsJoin",
    "Leave",
    "SmsjobsLeave",
    "UpdateSettings",
    "SmsjobsUpdateSettings",
    "GetStatus",
    "SmsjobsGetStatus",
    "GetSmsJob",
    "SmsjobsGetSmsJob",
    "FinishJob",
    "SmsjobsFinishJob"
]
