from ...tl import types as _tp


BoostsList = getattr(_tp, 'PremiumBoostsList', getattr(_tp, 'BoostsList', None))
PremiumBoostsList = getattr(_tp, 'PremiumBoostsList', None)
MyBoosts = getattr(_tp, 'PremiumMyBoosts', getattr(_tp, 'MyBoosts', None))
PremiumMyBoosts = getattr(_tp, 'PremiumMyBoosts', None)
BoostsStatus = getattr(_tp, 'PremiumBoostsStatus', getattr(_tp, 'BoostsStatus', None))
PremiumBoostsStatus = getattr(_tp, 'PremiumBoostsStatus', None)

__all__ = [
    "BoostsList",
    "PremiumBoostsList",
    "MyBoosts",
    "PremiumMyBoosts",
    "BoostsStatus",
    "PremiumBoostsStatus"
]
