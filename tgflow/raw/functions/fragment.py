from ...tl import functions as _fn


GetCollectibleInfo = getattr(_fn, 'GetCollectibleInfo', getattr(_fn, 'FragmentGetCollectibleInfo', None))
FragmentGetCollectibleInfo = getattr(_fn, 'FragmentGetCollectibleInfo', None)

__all__ = [
    "GetCollectibleInfo",
    "FragmentGetCollectibleInfo"
]
