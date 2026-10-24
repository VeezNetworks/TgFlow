from ...tl import functions as _fn


GetLangPack = getattr(_fn, 'GetLangPack', getattr(_fn, 'LangpackGetLangPack', None))
LangpackGetLangPack = getattr(_fn, 'LangpackGetLangPack', None)
GetStrings = getattr(_fn, 'GetStrings', getattr(_fn, 'LangpackGetStrings', None))
LangpackGetStrings = getattr(_fn, 'LangpackGetStrings', None)
GetDifference = getattr(_fn, 'GetDifference', getattr(_fn, 'LangpackGetDifference', None))
LangpackGetDifference = getattr(_fn, 'LangpackGetDifference', None)
GetLanguages = getattr(_fn, 'GetLanguages', getattr(_fn, 'LangpackGetLanguages', None))
LangpackGetLanguages = getattr(_fn, 'LangpackGetLanguages', None)
GetLanguage = getattr(_fn, 'GetLanguage', getattr(_fn, 'LangpackGetLanguage', None))
LangpackGetLanguage = getattr(_fn, 'LangpackGetLanguage', None)

__all__ = [
    "GetLangPack",
    "LangpackGetLangPack",
    "GetStrings",
    "LangpackGetStrings",
    "GetDifference",
    "LangpackGetDifference",
    "GetLanguages",
    "LangpackGetLanguages",
    "GetLanguage",
    "LangpackGetLanguage"
]
