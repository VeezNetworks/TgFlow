from ...tl import types as _tp


BotInfo = getattr(_tp, 'BotsBotInfo', getattr(_tp, 'BotInfo', None))
BotsBotInfo = getattr(_tp, 'BotsBotInfo', None)
PopularAppBots = getattr(_tp, 'BotsPopularAppBots', getattr(_tp, 'PopularAppBots', None))
BotsPopularAppBots = getattr(_tp, 'BotsPopularAppBots', None)
PreviewInfo = getattr(_tp, 'BotsPreviewInfo', getattr(_tp, 'PreviewInfo', None))
BotsPreviewInfo = getattr(_tp, 'BotsPreviewInfo', None)
ExportedBotToken = getattr(_tp, 'BotsExportedBotToken', getattr(_tp, 'ExportedBotToken', None))
BotsExportedBotToken = getattr(_tp, 'BotsExportedBotToken', None)
RequestedButton = getattr(_tp, 'BotsRequestedButton', getattr(_tp, 'RequestedButton', None))
BotsRequestedButton = getattr(_tp, 'BotsRequestedButton', None)
AccessSettings = getattr(_tp, 'BotsAccessSettings', getattr(_tp, 'AccessSettings', None))
BotsAccessSettings = getattr(_tp, 'BotsAccessSettings', None)

__all__ = [
    "BotInfo",
    "BotsBotInfo",
    "PopularAppBots",
    "BotsPopularAppBots",
    "PreviewInfo",
    "BotsPreviewInfo",
    "ExportedBotToken",
    "BotsExportedBotToken",
    "RequestedButton",
    "BotsRequestedButton",
    "AccessSettings",
    "BotsAccessSettings"
]
