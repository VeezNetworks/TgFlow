from ...tl import functions as _fn


CreateStickerSet = getattr(_fn, 'CreateStickerSet', getattr(_fn, 'StickersCreateStickerSet', None))
StickersCreateStickerSet = getattr(_fn, 'StickersCreateStickerSet', None)
RemoveStickerFromSet = getattr(_fn, 'RemoveStickerFromSet', getattr(_fn, 'StickersRemoveStickerFromSet', None))
StickersRemoveStickerFromSet = getattr(_fn, 'StickersRemoveStickerFromSet', None)
ChangeStickerPosition = getattr(_fn, 'ChangeStickerPosition', getattr(_fn, 'StickersChangeStickerPosition', None))
StickersChangeStickerPosition = getattr(_fn, 'StickersChangeStickerPosition', None)
AddStickerToSet = getattr(_fn, 'AddStickerToSet', getattr(_fn, 'StickersAddStickerToSet', None))
StickersAddStickerToSet = getattr(_fn, 'StickersAddStickerToSet', None)
SetStickerSetThumb = getattr(_fn, 'SetStickerSetThumb', getattr(_fn, 'StickersSetStickerSetThumb', None))
StickersSetStickerSetThumb = getattr(_fn, 'StickersSetStickerSetThumb', None)
CheckShortName = getattr(_fn, 'CheckShortName', getattr(_fn, 'StickersCheckShortName', None))
StickersCheckShortName = getattr(_fn, 'StickersCheckShortName', None)
SuggestShortName = getattr(_fn, 'SuggestShortName', getattr(_fn, 'StickersSuggestShortName', None))
StickersSuggestShortName = getattr(_fn, 'StickersSuggestShortName', None)
ChangeSticker = getattr(_fn, 'ChangeSticker', getattr(_fn, 'StickersChangeSticker', None))
StickersChangeSticker = getattr(_fn, 'StickersChangeSticker', None)
RenameStickerSet = getattr(_fn, 'RenameStickerSet', getattr(_fn, 'StickersRenameStickerSet', None))
StickersRenameStickerSet = getattr(_fn, 'StickersRenameStickerSet', None)
DeleteStickerSet = getattr(_fn, 'DeleteStickerSet', getattr(_fn, 'StickersDeleteStickerSet', None))
StickersDeleteStickerSet = getattr(_fn, 'StickersDeleteStickerSet', None)
ReplaceSticker = getattr(_fn, 'ReplaceSticker', getattr(_fn, 'StickersReplaceSticker', None))
StickersReplaceSticker = getattr(_fn, 'StickersReplaceSticker', None)

__all__ = [
    "CreateStickerSet",
    "StickersCreateStickerSet",
    "RemoveStickerFromSet",
    "StickersRemoveStickerFromSet",
    "ChangeStickerPosition",
    "StickersChangeStickerPosition",
    "AddStickerToSet",
    "StickersAddStickerToSet",
    "SetStickerSetThumb",
    "StickersSetStickerSetThumb",
    "CheckShortName",
    "StickersCheckShortName",
    "SuggestShortName",
    "StickersSuggestShortName",
    "ChangeSticker",
    "StickersChangeSticker",
    "RenameStickerSet",
    "StickersRenameStickerSet",
    "DeleteStickerSet",
    "StickersDeleteStickerSet",
    "ReplaceSticker",
    "StickersReplaceSticker"
]
