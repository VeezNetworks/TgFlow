from ...tl import types as _tp


ChannelParticipants = getattr(_tp, 'ChannelsChannelParticipants', getattr(_tp, 'ChannelParticipants', None))
ChannelsChannelParticipants = getattr(_tp, 'ChannelsChannelParticipants', None)
ChannelParticipantsNotModified = getattr(_tp, 'ChannelsChannelParticipantsNotModified', getattr(_tp, 'ChannelParticipantsNotModified', None))
ChannelsChannelParticipantsNotModified = getattr(_tp, 'ChannelsChannelParticipantsNotModified', None)
ChannelParticipant = getattr(_tp, 'ChannelsChannelParticipant', getattr(_tp, 'ChannelParticipant', None))
ChannelsChannelParticipant = getattr(_tp, 'ChannelsChannelParticipant', None)
AdminLogResults = getattr(_tp, 'ChannelsAdminLogResults', getattr(_tp, 'AdminLogResults', None))
ChannelsAdminLogResults = getattr(_tp, 'ChannelsAdminLogResults', None)
SendAsPeers = getattr(_tp, 'ChannelsSendAsPeers', getattr(_tp, 'SendAsPeers', None))
ChannelsSendAsPeers = getattr(_tp, 'ChannelsSendAsPeers', None)
SponsoredMessageReportResultChooseOption = getattr(_tp, 'ChannelsSponsoredMessageReportResultChooseOption', getattr(_tp, 'SponsoredMessageReportResultChooseOption', None))
ChannelsSponsoredMessageReportResultChooseOption = getattr(_tp, 'ChannelsSponsoredMessageReportResultChooseOption', None)
SponsoredMessageReportResultAdsHidden = getattr(_tp, 'ChannelsSponsoredMessageReportResultAdsHidden', getattr(_tp, 'SponsoredMessageReportResultAdsHidden', None))
ChannelsSponsoredMessageReportResultAdsHidden = getattr(_tp, 'ChannelsSponsoredMessageReportResultAdsHidden', None)
SponsoredMessageReportResultReported = getattr(_tp, 'ChannelsSponsoredMessageReportResultReported', getattr(_tp, 'SponsoredMessageReportResultReported', None))
ChannelsSponsoredMessageReportResultReported = getattr(_tp, 'ChannelsSponsoredMessageReportResultReported', None)

__all__ = [
    "ChannelParticipants",
    "ChannelsChannelParticipants",
    "ChannelParticipantsNotModified",
    "ChannelsChannelParticipantsNotModified",
    "ChannelParticipant",
    "ChannelsChannelParticipant",
    "AdminLogResults",
    "ChannelsAdminLogResults",
    "SendAsPeers",
    "ChannelsSendAsPeers",
    "SponsoredMessageReportResultChooseOption",
    "ChannelsSponsoredMessageReportResultChooseOption",
    "SponsoredMessageReportResultAdsHidden",
    "ChannelsSponsoredMessageReportResultAdsHidden",
    "SponsoredMessageReportResultReported",
    "ChannelsSponsoredMessageReportResultReported"
]
