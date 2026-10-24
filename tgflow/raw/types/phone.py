from ...tl import types as _tp


PhoneCall = getattr(_tp, 'PhonePhoneCall', getattr(_tp, 'PhoneCall', None))
PhonePhoneCall = getattr(_tp, 'PhonePhoneCall', None)
GroupCall = getattr(_tp, 'PhoneGroupCall', getattr(_tp, 'GroupCall', None))
PhoneGroupCall = getattr(_tp, 'PhoneGroupCall', None)
GroupParticipants = getattr(_tp, 'PhoneGroupParticipants', getattr(_tp, 'GroupParticipants', None))
PhoneGroupParticipants = getattr(_tp, 'PhoneGroupParticipants', None)
JoinAsPeers = getattr(_tp, 'PhoneJoinAsPeers', getattr(_tp, 'JoinAsPeers', None))
PhoneJoinAsPeers = getattr(_tp, 'PhoneJoinAsPeers', None)
ExportedGroupCallInvite = getattr(_tp, 'PhoneExportedGroupCallInvite', getattr(_tp, 'ExportedGroupCallInvite', None))
PhoneExportedGroupCallInvite = getattr(_tp, 'PhoneExportedGroupCallInvite', None)
GroupCallStreamChannels = getattr(_tp, 'PhoneGroupCallStreamChannels', getattr(_tp, 'GroupCallStreamChannels', None))
PhoneGroupCallStreamChannels = getattr(_tp, 'PhoneGroupCallStreamChannels', None)
GroupCallStreamRtmpUrl = getattr(_tp, 'PhoneGroupCallStreamRtmpUrl', getattr(_tp, 'GroupCallStreamRtmpUrl', None))
PhoneGroupCallStreamRtmpUrl = getattr(_tp, 'PhoneGroupCallStreamRtmpUrl', None)
GroupCallStars = getattr(_tp, 'PhoneGroupCallStars', getattr(_tp, 'GroupCallStars', None))
PhoneGroupCallStars = getattr(_tp, 'PhoneGroupCallStars', None)

__all__ = [
    "PhoneCall",
    "PhonePhoneCall",
    "GroupCall",
    "PhoneGroupCall",
    "GroupParticipants",
    "PhoneGroupParticipants",
    "JoinAsPeers",
    "PhoneJoinAsPeers",
    "ExportedGroupCallInvite",
    "PhoneExportedGroupCallInvite",
    "GroupCallStreamChannels",
    "PhoneGroupCallStreamChannels",
    "GroupCallStreamRtmpUrl",
    "PhoneGroupCallStreamRtmpUrl",
    "GroupCallStars",
    "PhoneGroupCallStars"
]
