from ...tl import functions as _fn


GetBoostsList = getattr(_fn, 'GetBoostsList', getattr(_fn, 'PremiumGetBoostsList', None))
PremiumGetBoostsList = getattr(_fn, 'PremiumGetBoostsList', None)
GetMyBoosts = getattr(_fn, 'GetMyBoosts', getattr(_fn, 'PremiumGetMyBoosts', None))
PremiumGetMyBoosts = getattr(_fn, 'PremiumGetMyBoosts', None)
ApplyBoost = getattr(_fn, 'ApplyBoost', getattr(_fn, 'PremiumApplyBoost', None))
PremiumApplyBoost = getattr(_fn, 'PremiumApplyBoost', None)
GetBoostsStatus = getattr(_fn, 'GetBoostsStatus', getattr(_fn, 'PremiumGetBoostsStatus', None))
PremiumGetBoostsStatus = getattr(_fn, 'PremiumGetBoostsStatus', None)
GetUserBoosts = getattr(_fn, 'GetUserBoosts', getattr(_fn, 'PremiumGetUserBoosts', None))
PremiumGetUserBoosts = getattr(_fn, 'PremiumGetUserBoosts', None)

__all__ = [
    "GetBoostsList",
    "PremiumGetBoostsList",
    "GetMyBoosts",
    "PremiumGetMyBoosts",
    "ApplyBoost",
    "PremiumApplyBoost",
    "GetBoostsStatus",
    "PremiumGetBoostsStatus",
    "GetUserBoosts",
    "PremiumGetUserBoosts"
]
