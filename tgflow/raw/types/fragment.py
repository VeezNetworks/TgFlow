from ...tl import types as _tp


CollectibleInfo = getattr(_tp, 'FragmentCollectibleInfo', getattr(_tp, 'CollectibleInfo', None))
FragmentCollectibleInfo = getattr(_tp, 'FragmentCollectibleInfo', None)

__all__ = [
    "CollectibleInfo",
    "FragmentCollectibleInfo"
]
