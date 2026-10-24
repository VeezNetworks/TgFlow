from ...tl import functions as _fn


EditPeerFolders = getattr(_fn, 'EditPeerFolders', getattr(_fn, 'FoldersEditPeerFolders', None))
FoldersEditPeerFolders = getattr(_fn, 'FoldersEditPeerFolders', None)

__all__ = [
    "EditPeerFolders",
    "FoldersEditPeerFolders"
]
