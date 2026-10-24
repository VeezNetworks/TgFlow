from ...tl import types as _tp


SuggestedShortName = getattr(_tp, 'StickersSuggestedShortName', getattr(_tp, 'SuggestedShortName', None))
StickersSuggestedShortName = getattr(_tp, 'StickersSuggestedShortName', None)

__all__ = [
    "SuggestedShortName",
    "StickersSuggestedShortName"
]
