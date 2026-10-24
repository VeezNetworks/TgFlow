from ...tl import types as _tp


TonesNotModified = getattr(_tp, 'AicomposeTonesNotModified', getattr(_tp, 'TonesNotModified', None))
AicomposeTonesNotModified = getattr(_tp, 'AicomposeTonesNotModified', None)
Tones = getattr(_tp, 'AicomposeTones', getattr(_tp, 'Tones', None))
AicomposeTones = getattr(_tp, 'AicomposeTones', None)

__all__ = [
    "TonesNotModified",
    "AicomposeTonesNotModified",
    "Tones",
    "AicomposeTones"
]
